from fastapi import APIRouter, Depends, HTTPException, status, Path
from sqlalchemy.orm import Session
from Models.Models import BSC_PAIS
from Schemas.BSC_PAIS import BSC_PAISSchema, BSC_PAISSchemaPost
from db import get_db


route = APIRouter(prefix="/BSC_PAIS", tags=["BSC_PAIS"])


@route.get('/')
async def GetAllPais(db: Session = Depends(get_db)):
    paises = db.query(BSC_PAIS).all()
    return [BSC_PAISSchema(ID_PAIS=pais.id_pais, NOMB_PAIS=pais.nomb_pais) for pais in paises]


@route.get("/{id_pais}")
async def GetPais(id_pais: int = Path(..., ge=1), db: Session = Depends(get_db)):
    pais = db.query(BSC_PAIS).get(id_pais)
    if pais is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return BSC_PAISSchema(ID_PAIS=pais.id_pais, NOMB_PAIS=pais.nomb_pais)


@route.post("/")
async def PostPais(bsc_pais_schema_post: BSC_PAISSchemaPost, db: Session = Depends(get_db)):
    pais = BSC_PAIS(nomb_pais=bsc_pais_schema_post.NOMB_PAIS)
    db.add(pais)
    db.commit()
    db.refresh(pais)
    return pais
