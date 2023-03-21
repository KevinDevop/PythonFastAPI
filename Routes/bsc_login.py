from fastapi import APIRouter, HTTPException, status, Depends
from fastapi.security import OAuth2PasswordRequestForm, OAuth2PasswordBearer
from sqlalchemy.orm import session
from db import get_db
from Models.Models import BSC_LOGIN, BSC_USUARIO
from Schemas.BSC_LOGIN import BSC_LOGIN_SCHEMA, LOGIN_SCHEMA, BSC_LOGIN_POST_SCHEMA, Token
from Schemas.BSC_USUARIO import BSC_USUARIO_SCHEMA
from sendemail import codigoEmail
from bcrypt import gensalt, hashpw, checkpw
from sqlalchemy.exc import SQLAlchemyError
from jwt import ACCESS_TOKEN_EXPIRE_MINUTES, createToken, getCurrrentActiveUser
from datetime import timedelta
import random


route = APIRouter(prefix="/BSC_LOGIN", tags=["BSC_LOGIN"])


@route.get("/", description="Lista los registro de bsc_login")
async def getLogin(db: session = Depends(get_db), token: BSC_USUARIO_SCHEMA = Depends(getCurrrentActiveUser)):
    users = db.query(BSC_LOGIN).all()

    return [BSC_LOGIN_SCHEMA(
        ID_LOGIN=user.id_login,
        EMAIL_CORPORATIVO_LOGIN=user.email_corporativo_login,
        CONTRASEÑA_LOGIN=user.contraseña_login,
        ID_USUARIO=user.id_usuario,
        VERIFICACION_LOGIN=user.verificacion_login,
        COD_VERIFICACION_LOGIN=user.cod_verificacion_login)
        for user in users]


@route.put("/verificacion/{email}", description="Verificación de correo")
async def putVerificacionCorreo(email: str, codigo: str, db: session = Depends(get_db)):
    buscar_correo = db.query(BSC_LOGIN).filter(
        BSC_LOGIN.email_corporativo_login == email).first()

    if not buscar_correo:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Correo no encotrado")

    if buscar_correo.cod_verificacion_login != codigo:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Codigo Invalido")

    buscar_correo.verificacion_login = True
    db.commit()

    return {"Message": "Correo Verificado"}


@route.post("/", description="Crea un registro de un usuario")
async def registroLogin(login: BSC_LOGIN_POST_SCHEMA, db: session = Depends(get_db)):
    salt = gensalt()
    hashed_password = hashpw(login.CONTRASEÑA_LOGIN.encode('utf-8'), salt)

    codigo_verificacion = ''.join(
        [str(random.randint(0, 9)) for _ in range(5)])

    db_registro = BSC_LOGIN(
        email_corporativo_login=login.EMAIL_CORPORATIVO_LOGIN,
        contraseña_login=hashed_password,
        id_usuario=login.ID_USUARIO,
        verificacion_login=False,
        cod_verificacion_login=codigo_verificacion
    )

    try:
        with db.begin():
            db.add(db_registro)
            db.flush()
            codigoEmail(login.EMAIL_CORPORATIVO_LOGIN, codigo_verificacion)
    except SQLAlchemyError as e:
        raise e

    return db_registro


@route.post("/login", response_model=Token, description="Inicio de sesión!")
async def Login(db: session = Depends(get_db), form_data: OAuth2PasswordRequestForm = Depends()):
    user = db.query(BSC_LOGIN).filter(
        BSC_LOGIN.email_corporativo_login == form_data.username).first()

    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales invalidas ☠️")

    if not user.verificacion_login:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                            detail="Su correo no ha sido validado.")

    if not checkpw(form_data.password.encode('utf-8'), user.contraseña_login.encode('utf-8')):
        raise HTTPException(status.HTTP_401_UNAUTHORIZED,
                            detail="Credenciales invalidas ☠️")

    info = db.query(BSC_USUARIO).filter(
        BSC_USUARIO.id_usuario == user.id_usuario).first()

    access_token_expire = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = createToken(
        {"id_usuario": user.id_usuario,
         "nombre": info.nombre_apellido_usuario,
         "id_rol": info.id_rol},
        access_token_expire)

    return {"access_token": access_token, "token_type": "bearer"}
