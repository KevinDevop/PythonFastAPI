from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from Models.Models import BSC_CIUDAD, BSC_DEPARTAMENTO
from Schemas.BSC_CIUDAD import BSC_CIUDAD_SCHEMA, BSC_CIUDAD_DEPARTAMENTO_SCHEMA, BSC_CIUDAD_POST_SCHEMA
from db import get_db


route = APIRouter(prefix="/BSC_CIUDAD", tags=["BSC_CIUDAD"])


@route.get("/", description="Retorna todas las ciudades")
async def getCiudad(db: Session = Depends(get_db)):
    ciudades = db.query(BSC_CIUDAD).all()

    return [BSC_CIUDAD_SCHEMA(ID_CIUDAD=ciudad.id_ciudad, NOMBRE_CIUDAD=ciudad.nombre_ciudad, ID_DEPARTAMENTO=ciudad.id_departamento)for ciudad in ciudades]


@route.get("/DEPARTAMENTO", description="Retorna todas las ciuidades con su respectivo departamento")
async def GetCiudadesDepartameto(db: Session = Depends(get_db)):
    ciudades = db.query(BSC_CIUDAD, BSC_DEPARTAMENTO).join(
        BSC_DEPARTAMENTO, BSC_CIUDAD.id_departamento == BSC_DEPARTAMENTO.id_departamento).all()

    result = [BSC_CIUDAD_DEPARTAMENTO_SCHEMA(ID_CIUDAD=ciudad.id_ciudad,
                                             NOMBRE_CIUDAD=ciudad.nombre_ciudad,
                                             NOMBRE_DEPARTAMENTO=departamento.nombre_departamento) for ciudad, departamento in ciudades]

    return result


@route.get('/{nombre_ciudad}', description="Retorna la busqueda de una ciudad o ciudades por su nombre, o similar")
async def GetFindCiudad(nombre_ciudad: str, db: Session = Depends(get_db)):
    ciudades = db.query(BSC_CIUDAD).filter(
        BSC_CIUDAD.nombre_ciudad.like(f"%{nombre_ciudad}%")).all()

    if not ciudades:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Not Found")

    return [BSC_CIUDAD_SCHEMA(ID_CIUDAD=ciudad.id_ciudad, NOMBRE_CIUDAD=ciudad.nombre_ciudad, ID_DEPARTAMENTO=ciudad.id_departamento)for ciudad in ciudades]


@route.post("/", description="Crea un registro de una ciudad")
async def postCiudad(ciudad_post: BSC_CIUDAD_POST_SCHEMA, db: Session = Depends(get_db)):
    ciudad = BSC_CIUDAD(nombre_ciudad=ciudad_post.NOMBRE_CIUDAD,
                        id_departamento=ciudad_post.ID_DEPARTAMENTO)
    db.add(ciudad)
    db.commit()
    db.refresh(ciudad)

    return ciudad


@route.put("/{id_ciudad}", description="Modifica una ciudad")
def putCiudad(id_ciudad: int, ciudad_post: BSC_CIUDAD_POST_SCHEMA, db: Session = Depends(get_db)):
    ciudad = db.query(BSC_CIUDAD).filter(
        BSC_CIUDAD.id_ciudad == id_ciudad).first()
    if not ciudad:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    ciudad.nombre_ciudad = ciudad_post.NOMBRE_CIUDAD
    ciudad.id_departamento = ciudad_post.ID_DEPARTAMENTO

    db.commit()
    db.refresh(ciudad)

    return ciudad
