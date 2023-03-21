from pydantic import BaseModel


class BSC_DEPARTAMENTOSchema(BaseModel):
    ID_DEPARTAMENTO: int
    NOMBRE_DEPARTAMENTO: str
    ID_PAIS: int


class BSC_DEPARTAMENTO_PAISSchema(BaseModel):
    ID_DEPARTAMENTO: int
    NOMBRE_DEPARTAMENTO: str
    NOMBRE_PAIS: str
