from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from Models.Models import BSC_ROL
from Schemas.BSC_ROL import BSC_ROL_SCHEMA
from db import get_db


route = APIRouter(prefix="/BSC_ROL", tags=["BSC_ROL"])


@route.get("/", description="Obtiene todos los roles.")
async def getRol(db: Session = Depends(get_db)):
    roles = db.query(BSC_ROL).all()

    return [BSC_ROL_SCHEMA(ID_ROL=rol.id_rol, DESC_ROL=rol.desc_rol)for rol in roles]
