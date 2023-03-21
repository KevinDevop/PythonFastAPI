from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from db import get_db
from Models.Models import MAP_PISO
from Schemas.MAP_PISO import MAP_PISOSSchema


route = APIRouter(prefix="/MAP_PISO", tags=["MAP_PISO"])


@route.get("/")
async def GetPisos(db: Session = Depends(get_db)):
    pisos = db.query(MAP_PISO).all()
    return [MAP_PISOSSchema(ID_PISO=piso.id_piso,  DESC_PISO=piso.desc_piso) for piso in pisos]


@route.get("/{id_piso}")
async def FindPisos(id_piso: int, db: Session = Depends(get_db)):
    piso = db.query(MAP_PISO).get(id_piso)
    if piso is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
    return MAP_PISOSSchema(ID_PISO=piso.id_piso, DESC_PISO=piso.desc_piso)
