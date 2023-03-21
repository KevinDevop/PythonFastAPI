from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from db import get_db
from Models.Models import BSC_BITACORA
from Schemas.BSC_BITACORA import BSC_BITACORA_SCHEMA


route = APIRouter(prefix="/BSC_BITACORA", tags=["BSC_BITACORA"])


@route.get("/", description="Lista todas las bitacoras")
async def getBitacoras(db: Session = Depends(get_db)):
    bitacoras = db.query(BSC_BITACORA).all()

    return [BSC_BITACORA_SCHEMA(
        ID_BITACORA=bitacora.id_bitacora,
        ACCION_BITACORA=bitacora.accion_bitacora,
        DESCRIPCION_BITACORA=bitacora.descripcion_bitacora,
        FECHA_CREACION_BITACORA=bitacora.fecha_creacion_bitacora,
        ID_USUARIO=bitacora.id_usuario
    )for bitacora in bitacoras]
