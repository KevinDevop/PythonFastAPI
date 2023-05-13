from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from Models.Models import BSC_GENERO
from Schemas.BSC_GENERO import BscGeneroSchema
from db import get_db

route = APIRouter(prefix="/bsc_genero", tags=["BSC_GENERO"])


@route.get("/", description="Retorna todos los registros de la tabla BSC_GENERO")
async def GetBscGenero(db: Session = Depends(get_db)) -> list[BscGeneroSchema]:
    generos = db.query(BSC_GENERO).all()
    return [BscGeneroSchema.from_orm(genero) for genero in generos]
