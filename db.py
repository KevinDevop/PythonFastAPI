from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os

# Crear un motor de base de datos y una sesión para hacer consultas

SQL_ALCHEMY_DATABASE_URL = ("mssql+pyodbc://{}:{}@{}/{}"
                            "?driver=ODBC+Driver+17+for+SQL+Server").format(
                                os.environ['DB_USER'],
                                os.environ['DB_PASSWORD'],
                                os.environ['DB_HOST'],
                                os.environ['DB_NAME'],
)


def get_db():
    try:
        engine = create_engine(SQL_ALCHEMY_DATABASE_URL)
        SessionLocal = sessionmaker(bind=engine)
        session = SessionLocal()
        yield session
    finally:
        session.close()
