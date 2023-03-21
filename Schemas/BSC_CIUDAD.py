from pydantic import BaseModel, validator


class BSC_CIUDAD_SCHEMA(BaseModel):
    ID_CIUDAD: int
    NOMBRE_CIUDAD: str
    ID_DEPARTAMENTO: int


class BSC_CIUDAD_DEPARTAMENTO_SCHEMA(BaseModel):
    ID_CIUDAD: int
    NOMBRE_CIUDAD: str
    NOMBRE_DEPARTAMENTO: str


class BSC_CIUDAD_POST_SCHEMA(BaseModel):
    NOMBRE_CIUDAD: str
    ID_DEPARTAMENTO: int

    @validator("NOMBRE_CIUDAD")
    def NombreCiuidadNotBlank(cls, v):
        if not v.strip():
            raise ValueError("No puede estar en blanco")
        return v
