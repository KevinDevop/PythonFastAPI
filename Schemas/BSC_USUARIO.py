from pydantic import BaseModel
from datetime import date
from typing import Optional


class BSC_USUARIO_SCHEMA(BaseModel):
    ID_USUARIO: int
    NOMBRE_APELLIDO_USUARIO: str
    CEDULA_USUARIO: str
    FECHA_NACIMIENTO: date
    CORREO_PERSONAL_USUARIO: str
    DIRECCION_USUARIO: str
    ESTADO_LOGICO_USUARIO: bool
    TELEFONO_USUARIO: str
    FOTO_USUARIO: Optional[str] = None
    ID_ROL: int
    ID_CIUDAD: int
    ID_GENERO: int
    ID_ESTADO: int


class BSC_USUARIO_COMPLET_SCHEMA(BaseModel):
    ID_USUARIO: int
    NOMBRE_APELLIDO_USUARIO: str
    CEDULA_USUARIO: str
    FECHA_NACIMIENTO: date
    CORREO_PERSONAL_USUARIO: str
    DIRECCION_USUARIO: str
    ESTADO_LOGICO_USUARIO: int
    TELEFONO_USUARIO: str
    FOTO_USUARIO: Optional[str] = None
    ROL: str
    CIUDAD: str
    GENERO: str
    ESTADO: str


class BSC_USUARIO_POST_SCHEMA(BaseModel):
    NOMBRE_APELLIDO_USUARIO: str
    CEDULA_USUARIO: str
    FECHA_NACIMIENTO: date
    CORREO_PERSONAL_USUARIO: str
    DIRECCION_USUARIO: str
    ESTADO_LOGICO_USUARIO: int
    TELEFONO_USUARIO: str
    FOTO_USUARIO: Optional[str] = None
    ID_ROL: int
    ID_CIUDAD: int
    ID_GENERO: int
    ID_ESTADO: int
