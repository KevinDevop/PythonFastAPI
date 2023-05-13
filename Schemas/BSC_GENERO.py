from pydantic import BaseModel


class BscGeneroSchema(BaseModel):
    id_genero: int
    nomb_genero: str

    class Config:
        orm_mode = True
