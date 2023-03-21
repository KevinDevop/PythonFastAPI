from pydantic import BaseModel
from datetime import datetime


class MAP_ASISTENCIA_SCHEMA(BaseModel):
    ID_ASISTENCIA: int
    REGISTRO: datetime
    ID_PRACTICANTE: int

