from jose import jwt, JWTError
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta
from Schemas.BSC_LOGIN import TokenData
from Schemas.BSC_USUARIO import BSC_USUARIO_SCHEMA
from Models.Models import BSC_USUARIO
from sqlalchemy.orm import Session
from db import get_db
import os

SECRET_KEY = os.environ['SECRET_KEY']
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 10

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="BSC_LOGIN/login")


def createToken(data: dict, expires_delta: timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.utcnow() + expires_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({"exp": expire})
    encode_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encode_jwt


async def getCurrentUser(token: str = Depends(oauth2_scheme), db: Session = Depends(get_db)) -> BSC_USUARIO_SCHEMA:
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        id_usuario: int = payload.get("id_usuario")

        if id_usuario is None:
            raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                detail="Could no validate credentials", headers={"WWW-Authenticate": "Bearer"})
            
        token_data = TokenData(id_usuario=id_usuario)
    except JWTError as e:
        print(e)
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Could no validate credentials", headers={"WWW-Authenticate": "Bearer"})
    user = await getFindUsuario(token_data.id_usuario, db)
    if user is None:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Could no valixdate credentials", headers={"WWW-Authenticate": "Bearer"})
    return user


async def getFindUsuario(id_usuario: int, db: Session):
    usuario = db.query(BSC_USUARIO).filter(
        BSC_USUARIO.id_usuario == id_usuario).first()

    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    result = BSC_USUARIO_SCHEMA(ID_USUARIO=usuario.id_usuario, NOMBRE_APELLIDO_USUARIO=usuario.nombre_apellido_usuario, CEDULA_USUARIO=usuario.cedula_usuario, FECHA_NACIMIENTO=usuario.fecha_nacimiento, CORREO_PERSONAL_USUARIO=usuario.correo_personal_usuario,
                                DIRECCION_USUARIO=usuario.direccion_usuario, ESTADO_LOGICO_USUARIO=usuario.estado_logico_usuario, TELEFONO_USUARIO=usuario.telefono_usuario, FOTO_USUARIO=usuario.foto_usuario, ID_ROL=usuario.id_rol, ID_CIUDAD=usuario.id_ciudad, ID_GENERO=usuario.id_genero, ID_ESTADO=usuario.id_estado)
    print(result)
    return result


async def getCurrrentActiveUser(current_usuer: BSC_USUARIO_SCHEMA = Depends(getCurrentUser)):
    if not current_usuer.ESTADO_LOGICO_USUARIO:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Activado")
    return current_usuer
