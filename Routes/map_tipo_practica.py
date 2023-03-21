from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.orm import Session
from Models.Models import MAP_TIPO_PRACTICA
from db import get_db


route = APIRouter(prefix="/MAP_TIPO_PRACTICA", tags=["MAP_TIPO_PRACTICA"])

