from pydantic import BaseModel, EmailStr
from typing import Optional


class BSC_LOGIN_SCHEMA(BaseModel):
    ID_LOGIN: int
    EMAIL_CORPORATIVO_LOGIN: str
    CONTRASEÑA_LOGIN: str
    ID_USUARIO: int
    VERIFICACION_LOGIN: bool
    COD_VERIFICACION_LOGIN: str


class BSC_LOGIN_VERIFY_SCHEMA(BaseModel):
    COD_VERIFICACION_LOGIN = str


class BSC_LOGIN_POST_SCHEMA(BaseModel):
    EMAIL_CORPORATIVO_LOGIN: str
    CONTRASEÑA_LOGIN: str
    ID_USUARIO: int


class LOGIN_SCHEMA(BaseModel):
    EMAIL_CORPORATIVO_LOGIN: str
    CONTRASEÑA_LOGIN: str


class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    id_usuario: int | None = None
