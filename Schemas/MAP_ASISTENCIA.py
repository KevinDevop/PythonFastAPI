from pydantic import BaseModel
from datetime import datetime


class MAP_ASISTENCIA_SCHEMA(BaseModel):
    id_asistencia: int
    registro: datetime
    id_practicante: int

    class Config:
        orm_mode = True
