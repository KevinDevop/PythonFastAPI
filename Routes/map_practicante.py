from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session, joinedload
from db import get_db
from Models.Models import MAP_PRACTICANTE
from Schemas.MAP_PRACTICANTE import MAP_PRACTICANTE_SCHEMA, MAP_PRACTICANTE_COMPLETE_SCHEMA
from jwt import getCurrrentActiveUser


route = APIRouter(prefix="/MAP_PRACTICANTE", tags=["MAP_PRACTICANTE"])


@route.get("/", description="Retorna toda la información de los practicantes.")
async def getPranticantes(db: Session = Depends(get_db), token: str = Depends(getCurrrentActiveUser)):
    practicantes = db.query(MAP_PRACTICANTE).all()

    result = [MAP_PRACTICANTE_SCHEMA(
        ID_PRACTICANTE=practicante.id_practicante,
        CODIGO_PRACTICANTE=practicante.codigo_practicante,
        DURACION_PRACTICA=practicante.duracion_practica,
        FECHA_INGRESO=practicante.fecha_ingreso,
        ACCESO_BIOMETRICO=practicante.acceso_biometrico,
        ID_TIPO_PRACTICA=practicante.id_tipo_practica,
        ID_INSTITUCION=practicante.id_institucion,
        ID_PISO=practicante.id_piso,
        ID_LIDER_FUNCIONAL=practicante.id_lider_funcional,
        ID_LIDER_ADMINISTRATIVO=practicante.id_lider_administrativo,
        ID_LIDER_ENTRENAMIENTO=practicante.id_lider_entrenamiento,
        ID_USUARIO=practicante.id_usuario
    )for practicante in practicantes]

    return result


@route.get("/COMPLETE")
async def getCompletePracticantes(db: Session = Depends(get_db)):
    practicantes = db.query(MAP_PRACTICANTE).options(
        joinedload(MAP_PRACTICANTE.institucion),
        joinedload(MAP_PRACTICANTE.piso),
        joinedload(MAP_PRACTICANTE.tipo_practica),
        joinedload(MAP_PRACTICANTE.entrenamiento),
        joinedload(MAP_PRACTICANTE.funcional),
        joinedload(MAP_PRACTICANTE.administrativo),
        joinedload(MAP_PRACTICANTE.usuario)
    ).all()

    result = [
        MAP_PRACTICANTE_COMPLETE_SCHEMA(
            ID_PRACTICANTE=practicante.id_practicante,
            CODIGO_PRACTICANTE=practicante.codigo_practicante,
            DURACION_PRACTICA=practicante.duracion_practica,
            FECHA_INGRESO=practicante.fecha_ingreso,
            ACCESO_BIOMETRICO=practicante.acceso_biometrico,
            TIPO_PRACTICA=practicante.tipo_practica.desc_practica,
            INSTITUCION=practicante.institucion.nomb_institucion,
            PISO=practicante.piso.desc_piso,
            LIDER_ADMINISTRATIVO=practicante.administrativo.nombre_administrativo,
            LIDER_ENTRENAMIENTO=practicante.entrenamiento.nombre_entrenamiento,
            LIDER_FUNCIONAL=practicante.funcional.nombre_funcional,
            USUARIO=practicante.usuario.nombre_apellido_usuario
        )
        for practicante in practicantes
    ]

    return result
