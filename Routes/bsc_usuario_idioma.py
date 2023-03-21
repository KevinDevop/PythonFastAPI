from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from Models.Models import BSC_USUARIO_IDIOMA
from Schemas.BSC_USUARIO_IDIOMA import BSC_USUARIO_IDIOMA_SCHEMA
from db import get_db


route = APIRouter(prefix="/BSC_USUARIO_IDIOMA", tags=["BSC_USUARIO_IDIOMA"])


@route.get("/", description="Obtiene todos los registros")
async def getBscUsuarioIdioma(db: Session = Depends(get_db)):
    usuariosIdiomas = db.query(BSC_USUARIO_IDIOMA).all()

    return [BSC_USUARIO_IDIOMA_SCHEMA(ID=usuarioIdioma.id, ID_IDIOMA=usuarioIdioma.id_idioma, ID_USUARIO=usuarioIdioma.id_usuario) for usuarioIdioma in usuariosIdiomas]
