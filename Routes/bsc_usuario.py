from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session, joinedload
from Models.Models import BSC_USUARIO
from Schemas.BSC_USUARIO import BSC_USUARIO_SCHEMA, BSC_USUARIO_COMPLET_SCHEMA, BSC_USUARIO_POST_SCHEMA
from db import get_db


route = APIRouter(prefix="/BSC_USUARIO", tags=["BSC_USUARIO"])


@route.get("/")
async def getUsuario(db: Session = Depends(get_db)):
    usuarios = db.query(BSC_USUARIO).all()

    return [BSC_USUARIO_SCHEMA(ID_USUARIO=usuario.id_usuario, NOMBRE_APELLIDO_USUARIO=usuario.nombre_apellido_usuario, CEDULA_USUARIO=usuario.cedula_usuario, FECHA_NACIMIENTO=usuario.fecha_nacimiento, CORREO_PERSONAL_USUARIO=usuario.correo_personal_usuario, DIRECCION_USUARIO=usuario.direccion_usuario, ESTADO_LOGICO_USUARIO=usuario.estado_logico_usuario, TELEFONO_USUARIO=usuario.telefono_usuario, FOTO_USUARIO=usuario.foto_usuario, ID_ROL=usuario.id_rol, ID_CIUDAD=usuario.id_ciudad, ID_GENERO=usuario.id_genero, ID_ESTADO=usuario.id_estado)for usuario in usuarios]


@route.get('/BuscarUsuario/{id_usuario}')
async def getFindUsuario(id_usuario: int, db: Session = Depends(get_db)):
    usuario = db.query(BSC_USUARIO).get(id_usuario)

    if usuario is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    return BSC_USUARIO_SCHEMA(ID_USUARIO=usuario.id_usuario, NOMBRE_APELLIDO_USUARIO=usuario.nombre_apellido_usuario, CEDULA_USUARIO=usuario.cedula_usuario, FECHA_NACIMIENTO=usuario.fecha_nacimiento, CORREO_PERSONAL_USUARIO=usuario.correo_personal_usuario, DIRECCION_USUARIO=usuario.direccion_usuario, ESTADO_LOGICO_USUARIO=usuario.estado_logico_usuario, TELEFONO_USUARIO=usuario.telefono_usuario, FOTO_USUARIO=usuario.foto_usuario, ID_ROL=usuario.id_rol, ID_CIUDAD=usuario.id_ciudad, ID_GENERO=usuario.id_genero, ID_ESTADO=usuario.id_estado)


@route.get("/COMPLETE", description="Retorna el usuario con sus respectivos detalles de las tablas anidadas.")
async def getUsarioComplet(db: Session = Depends(get_db)):
    usuarios = db.query(BSC_USUARIO).options(
        joinedload(BSC_USUARIO.genero),
        joinedload(BSC_USUARIO.rol),
        joinedload(BSC_USUARIO.estado),
        joinedload(BSC_USUARIO.ciudad)
    ).all()

    result = [BSC_USUARIO_COMPLET_SCHEMA(
        ID_USUARIO=usuario.id_usuario,
        NOMBRE_APELLIDO_USUARIO=usuario.nombre_apellido_usuario,
        CEDULA_USUARIO=usuario.cedula_usuario,
        FECHA_NACIMIENTO=usuario.fecha_nacimiento,
        CORREO_PERSONAL_USUARIO=usuario.correo_personal_usuario,
        DIRECCION_USUARIO=usuario.direccion_usuario,
        ESTADO_LOGICO_USUARIO=usuario.estado_logico_usuario,
        TELEFONO_USUARIO=usuario.telefono_usuario,
        FOTO_USUARIO=usuario.foto_usuario,
        ROL=usuario.rol.desc_rol,
        CIUDAD=usuario.ciudad.nombre_ciudad,
        GENERO=usuario.genero.nomb_genero,
        ESTADO=usuario.estado.nomb_estado
    )
        for usuario in usuarios]

    return result

    # usuarios = db.query(BSC_USUARIO, BSC_GENERO, BSC_ROL, BSC_CIUDAD, BSC_ESTADO).join(
    #     BSC_GENERO, BSC_USUARIO.id_genero == BSC_GENERO.id_genero).join(BSC_ROL, BSC_USUARIO.id_rol == BSC_ROL.id_rol)\
    #     .join(BSC_CIUDAD, BSC_USUARIO.id_ciudad == BSC_CIUDAD.id_ciudad)\
    #     .join(BSC_ESTADO, BSC_USUARIO.id_estado == BSC_ESTADO.id_estado).all()

    # result = [BSC_USUARIO_COMPLET_SCHEMA(ID_USUARIO=usuario.id_usuario, NOMBRE_APELLIDO_USUARIO=usuario.nombre_apellido_usuario, CEDULA_USUARIO=usuario.cedula_usuario, FECHA_NACIMIENTO=usuario.fecha_nacimiento, CORREO_PERSONAL_USUARIO=usuario.correo_personal_usuario, DIRECCION_USUARIO=usuario.direccion_usuario,  ESTADO_LOGICO_USUARIO=usuario.estado_logico_usuario, TELEFONO_USUARIO=usuario.telefono_usuario, FOTO_USUARIO=usuario.foto_usuario, ROL=rol.desc_rol, CIUDAD=ciudad.nombre_ciudad, GENERO=genero.nomb_genero, ESTADO=estado.nomb_estado)
    #           for usuario, genero, rol, ciudad, estado in usuarios]

    # return result


@route.post("/", description="Guarda un registro de usuario.")
async def postUsuario(usuario_post_schema: BSC_USUARIO_POST_SCHEMA, db: Session = Depends(get_db)):
    usuario = BSC_USUARIO(
        nombre_apellido_usuario=usuario_post_schema.NOMBRE_APELLIDO_USUARIO,
        cedula_usuario=usuario_post_schema.CEDULA_USUARIO,
        fecha_nacimiento=usuario_post_schema.FECHA_NACIMIENTO,
        correo_personal_usuario=usuario_post_schema.CORREO_PERSONAL_USUARIO,
        direccion_usuario=usuario_post_schema.DIRECCION_USUARIO,
        estado_logico_usuario=usuario_post_schema.ESTADO_LOGICO_USUARIO,
        telefono_usuario=usuario_post_schema.TELEFONO_USUARIO,
        foto_usuario=usuario_post_schema.FOTO_USUARIO,
        id_rol=usuario_post_schema.ID_ROL,
        id_ciudad=usuario_post_schema.ID_CIUDAD,
        id_genero=usuario_post_schema.ID_GENERO,
        id_estado=usuario_post_schema.ID_ESTADO)

    db.add(usuario)
    db.commit()
    db.refresh(usuario)

    return usuario
