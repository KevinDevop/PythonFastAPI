from pydantic import BaseModel, validator


class BSC_CIUDAD_SCHEMA(BaseModel):
    id_ciudad: int
    nombre_ciudad: str
    id_departamento: int

    class Config:
        orm_mode = True


class BSC_CIUDAD_DEPARTAMENTO_SCHEMA(BaseModel):
    id_ciudad: int
    nombre_ciudad: str
    nombre_departamento: str

    class Config:
        orm_mode = True


class BSC_CIUDAD_POST_SCHEMA(BaseModel):
    NOMBRE_CIUDAD: str
    ID_DEPARTAMENTO: int

    @validator("NOMBRE_CIUDAD")
    def NombreCiuidadNotBlank(cls, v):
        if not v.strip():
            raise ValueError("No puede estar en blanco")
        return v
