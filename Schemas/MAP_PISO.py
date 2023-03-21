from pydantic import BaseModel


class MAP_PISOSSchema(BaseModel):
    ID_PISO: int
    DESC_PISO: str
