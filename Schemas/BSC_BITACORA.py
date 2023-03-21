from pydantic import BaseModel
from datetime import datetime


class BSC_BITACORA_SCHEMA(BaseModel):
    ID_BITACORA: int
    ACCION_BITACORA: str
    DESCRIPCION_BITACORA: str
    FECHA_CREACION_BITACORA: datetime
    ID_USUARIO: int
