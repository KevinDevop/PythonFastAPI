from pydantic import BaseModel


class MAP_ENTRENAMIENTO_SCHEMA(BaseModel):
    id_lider_entrenamiento: int
    nombre_entrenamiento: str

    class Config:
        orm_mode = True
