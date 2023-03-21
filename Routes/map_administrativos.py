from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from Models.Models import MAP_ADMINISTRATIVO
from Schemas.MAP_ADMINISTRATIVO import MAP_ADMINISTRATIVOSchema, MAP_ADMINISTRATIVOS_POST_SCHEMA

route = APIRouter(prefix="/MAP_ADMINISTRATIVOS", tags=["MAP_ADMINISTRATIVOS"])


@route.get("/")
async def GetAdministrativos(db: Session = Depends(get_db)):
    administrativos = db.query(MAP_ADMINISTRATIVO).all()
    return [MAP_ADMINISTRATIVOSchema(ID_LIDER_ADMINISTRATIVO=admin.id_lider_administrativo, NOMBRE_ADMINISTRATIVO=admin.nombre_administrativo)for admin in administrativos]


@route.post("/")
async def postAdministrativo(administrativo_post_schema: MAP_ADMINISTRATIVOS_POST_SCHEMA, db: Session = Depends(get_db)):
    administrativo = MAP_ADMINISTRATIVO(
        nombre_administrativo=administrativo_post_schema.NOMBRE_ADMINISTRATIVO)

    db.add(administrativo)
    db.commit()
    db.refresh(administrativo)

    return administrativo
