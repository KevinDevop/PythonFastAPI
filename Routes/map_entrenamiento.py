from fastapi import APIRouter, Depends
from sqlalchemy.orm import session
from Models.Models import MAP_ENTRENAMIENTO
from Schemas.MAP_ENTRENAMIENTO import MAP_ENTRENAMIENTO_SCHEMA
from db import get_db


route = APIRouter(prefix="/map_entrenamiento", tags=["MAP_ENTRENAMIENTO"])


@route.get("/", description="Obtiene todos los registro de la tabla Map_Entrenamiento", response_model=list[MAP_ENTRENAMIENTO_SCHEMA])
async def getMapEntrenamient(db: session = Depends(get_db)):
    mapEntrenamiento = db.query(MAP_ENTRENAMIENTO).all()

    return [MAP_ENTRENAMIENTO_SCHEMA.from_orm(mapEntrenamiento) for mapEntrenamiento in mapEntrenamiento]
