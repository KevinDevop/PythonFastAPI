from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from Models.Models import MAP_ASISTENCIA
from Schemas.MAP_ASISTENCIA import MAP_ASISTENCIA_SCHEMA
from db import get_db
import pandas as pd
from functools import lru_cache
route = APIRouter(prefix="/MAP_ASISTENCIA", tags=["MAP_ASISTENCIA"])


@route.get("/", description="Obtiene todos los registros de Asistencia")
async def getMapAsistencia(db: Session = Depends(get_db)) -> list[MAP_ASISTENCIA_SCHEMA]:
    asistencias = db.query(MAP_ASISTENCIA).all()

    return [MAP_ASISTENCIA_SCHEMA.from_orm(asistencia) for asistencia in asistencias]

    # query = db.query(MAP_ASISTENCIA.id_asistencia,
    #                  MAP_ASISTENCIA.registro, MAP_ASISTENCIA.id_practicante)

    # asistencia = query.order_by(MAP_ASISTENCIA.id_asistencia).paginate(
    #     page=skip, per_page=limit)

    # return {
    #     "data": [MAP_ASISTENCIA_SCHEMA(ID_ASISTENCIA=asistencia.id_asistencia, REGISTRO=asistencia.registro, ID_PRACTICANTE=asistencia.id_practicante) for asistencia in asistencia.items],
    #     "total": asistencia.total,
    #     "pages": asistencia.pages,
    #     "page": asistencia.page,
    #     "per_page": asistencia.per_page,
    # }


@route.post("/CARGAR_REGISTROS", description="Se cargan las asistencias de los practicantes.")
async def postCargaResgistros(filename: str, db: Session = Depends(get_db)):
    try:

        asistenciaRegistro = []

        file = pd.read_excel(filename)
        data = file.to_dict('records')

        for row in data:
            registro = row["REGISTRO"]
            id_practicante = row["ID_PRACTICANTE"]

            existeRegistro = db.query(MAP_ASISTENCIA).filter(
                MAP_ASISTENCIA.registro == registro).first()

            if existeRegistro:
                continue

            asistencia = MAP_ASISTENCIA(
                registro=registro, id_practicante=id_practicante)
            asistenciaRegistro.append(asistencia)

        db.bulk_save_objects(asistenciaRegistro)
        db.commit()

        return {"mensaje": "Los datos se cargaron correctamente"}
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
