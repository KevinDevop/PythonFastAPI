from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db import get_db
from Models.Models import BSC_DEPARTAMENTO, BSC_PAIS
from Schemas.BSC_DEPARTAMENTO import BSC_DEPARTAMENTOSchema, BSC_DEPARTAMENTO_PAISSchema

route = APIRouter(prefix="/BSC_DEPARTAMENTO", tags=["BSC_DEPARTAMENTO"])


@route.get("/")
async def GetDepartamentos(db: Session = Depends(get_db)):
    departamentos = db.query(BSC_DEPARTAMENTO, BSC_PAIS).join(
        BSC_PAIS, BSC_DEPARTAMENTO.id_pais == BSC_PAIS.id_pais).all()

    result = [BSC_DEPARTAMENTO_PAISSchema(ID_DEPARTAMENTO=departamento.id_departamento,
                                          NOMBRE_DEPARTAMENTO=departamento.nombre_departamento, NOMBRE_PAIS=pais.nomb_pais)for departamento, pais in departamentos]

    if departamentos is None:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST)

    return result


@route.get("/{id_dep}")
async def GetFindDepartamento(id_dep: int, db: Session = Depends(get_db)):
    departameto = db.query(BSC_DEPARTAMENTO).filter(
        BSC_DEPARTAMENTO.id_departamento == id_dep).first()
    if departameto is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="No encontrado")
    return BSC_DEPARTAMENTOSchema(ID_DEPARTAMENTO=departameto.id_departamento, NOMBRE_DEPARTAMENTO=departameto.nombre_departamento, ID_PAIS=departameto.id_pais)


@route.get("/PAIS/{id_dep}", summary="Busca el departamento por su ID", description="Retorna el departamento y su pais por su ID")
async def GetFindDepartamentoComplete(id_dep: int, db: Session = Depends(get_db)):
    # departamento = db.query(BSC_DEPARTAMENTO).filter(
    #     BSC_DEPARTAMENTO.id_departamento == id_dep).first()
    # if departamento is None:
    #     raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    # pais = db.query(BSC_PAIS).filter(
    #     BSC_PAIS.id_pais == departamento.id_pais).first()

    departamento = db.query(BSC_DEPARTAMENTO.id_departamento,
                            BSC_DEPARTAMENTO.nombre_departamento,
                            BSC_PAIS.nomb_pais)\
        .join(BSC_PAIS, BSC_DEPARTAMENTO.id_pais == BSC_PAIS.id_pais)\
        .filter(BSC_DEPARTAMENTO.id_departamento == BSC_DEPARTAMENTO.id_departamento == id_dep).first()

    if departamento is None:
        raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Not Found")

    return BSC_DEPARTAMENTO_PAISSchema(ID_DEPARTAMENTO=departamento.id_departamento,
                                       NOMBRE_DEPARTAMENTO=departamento.nombre_departamento, NOMBRE_PAIS=departamento.nomb_pais)
