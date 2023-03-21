from pydantic import BaseModel


class BSC_IDIOMA_SCHEMA(BaseModel):
    ID_IDIOMA: int
    NOMBRE_IDIOMA: str


class BSC_IDIOMA_POST_SCHEMA(BaseModel):
    NOMBRE_IDIOMA: str