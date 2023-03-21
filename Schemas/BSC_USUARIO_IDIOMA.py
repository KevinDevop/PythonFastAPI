from pydantic import BaseModel


class BSC_USUARIO_IDIOMA_SCHEMA(BaseModel):
    ID: int
    ID_IDIOMA: int
    ID_USUARIO: int
