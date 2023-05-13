from sqlalchemy import Column, Integer, String, ForeignKey, DATE, SmallInteger, DATETIME
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship


Base = declarative_base()


class BSC_USUARIO(Base):
    __tablename__ = 'BSC_USUARIO'
    id_usuario = Column(Integer, primary_key=True, autoincrement=True)
    nombre_apellido_usuario = Column(String, nullable=False)
    cedula_usuario = Column(String, nullable=False)
    fecha_nacimiento = Column(DATE, nullable=False)
    correo_personal_usuario = Column(String, nullable=False)
    direccion_usuario = Column(String, nullable=False)
    estado_logico_usuario = Column(SmallInteger, nullable=False)
    telefono_usuario = Column(String, nullable=False)
    foto_usuario = Column(String)
    id_rol = Column(Integer, ForeignKey('BSC_ROL.id_rol'), nullable=False)
    id_ciudad = Column(Integer, ForeignKey(
        'BSC_CIUDAD.id_ciudad'), nullable=False)
    id_genero = Column(Integer, ForeignKey(
        'BSC_GENERO.id_genero'), nullable=False)
    id_estado = Column(Integer, ForeignKey(
        'BSC_ESTADO.id_estado'), nullable=False)
    genero = relationship("BSC_GENERO")
    rol = relationship("BSC_ROL")
    estado = relationship("BSC_ESTADO")
    ciudad = relationship("BSC_CIUDAD")
    practicante = relationship("MAP_PRACTICANTE", back_populates="usuario")


class BSC_PAIS(Base):
    __tablename__ = "BSC_PAIS"
    id_pais = Column(Integer, primary_key=True, autoincrement=True)
    nomb_pais = Column(String)


class BSC_DEPARTAMENTO(Base):
    __tablename__ = 'BSC_DEPARTAMENTO'
    id_departamento = Column(Integer, primary_key=True, autoincrement=True)
    nombre_departamento = Column(String, nullable=False)
    id_pais = Column(Integer, ForeignKey('BSC_PAIS.id_pais'), nullable=False)
    pais = relationship("BSC_PAIS")


class BSC_CIUDAD(Base):
    __tablename__ = 'BSC_CIUDAD'
    id_ciudad = Column(Integer, primary_key=True, autoincrement=True)
    nombre_ciudad = Column(String, nullable=False)
    id_departamento = Column(Integer, ForeignKey(
        'BSC_DEPARTAMENTO.id_departamento'), nullable=False)
    departamento = relationship("BSC_DEPARTAMENTO")


class BSC_IDIOMA(Base):
    __tablename__ = 'BSC_IDIOMA'
    id_idioma = Column(Integer, primary_key=True, autoincrement=True)
    nombre_idioma = Column(String, nullable=False)


class BSC_USUARIO_IDIOMA(Base):
    __tablename__ = 'BSC_USUARIO_IDIOMA'
    id = Column(Integer, primary_key=True, autoincrement=True)
    id_idioma = Column(Integer, nullable=False)
    id_usuario = Column(Integer, nullable=False)


class BSC_BITACORA(Base):
    __tablename__ = "BSC_BITACORA"
    id_bitacora = Column(Integer, primary_key=True, autoincrement=True)
    accion_bitacora = Column(String, nullable=False)
    descripcion_bitacora = Column(String, nullable=False)
    fecha_creacion_bitacora = Column(DATETIME, nullable=False)
    id_usuario = Column(Integer, ForeignKey(
        'BSC_USUARIO.id_usuario'), nullable=False)
    usuario = relationship("BSC_USUARIO")


class BSC_GENERO(Base):
    __tablename__ = "BSC_GENERO"
    id_genero = Column(Integer, primary_key=True)
    nomb_genero = Column(String, nullable=False)


class BSC_ESTADO(Base):
    __tablename__ = "BSC_ESTADO"
    id_estado = Column(Integer, primary_key=True)
    nomb_estado = Column(String, nullable=False)


class BSC_LOGIN(Base):
    __tablename__ = "BSC_LOGIN"
    id_login = Column(Integer, primary_key=True, index=True)
    email_corporativo_login = Column(String, nullable=False)
    contraseña_login = Column(String, nullable=False)
    id_usuario = Column(Integer, ForeignKey(
        'BSC_USUARIO.id_usuario'), nullable=False)
    verificacion_login = Column(SmallInteger, nullable=False)
    cod_verificacion_login = Column(String, nullable=False)
    usuario = relationship("BSC_USUARIO")


class BSC_ROL(Base):
    __tablename__ = "BSC_ROL"
    id_rol = Column(Integer, primary_key=True)
    desc_rol = Column(String, nullable=False)


class MAP_HORARIO(Base):
    __tablename__ = "MAP_HORARIO"
    id_horario = Column(Integer, primary_key=True)
    dia_horario = Column(String, nullable=False)


class MAP_TIPO_PRACTICA(Base):
    __tablename__ = "MAP_TIPO_PRACTICA"
    id_practica = Column(Integer, primary_key=True)
    desc_practica = Column(String, nullable=False)
    practicante = relationship(
        "MAP_PRACTICANTE", back_populates="tipo_practica")


class MAP_INSTITUCION(Base):
    __tablename__ = "MAP_INSTITUCION"
    id_institucion = Column(Integer, primary_key=True)
    nomb_institucion = Column(String, nullable=False)
    institucion = relationship("MAP_PRACTICANTE", back_populates="institucion")


class MAP_ENTRENAMIENTO(Base):
    __tablename__ = "MAP_ENTRENAMIENTO"
    id_lider_entrenamiento = Column(Integer, primary_key=True)
    nombre_entrenamiento = Column(String, nullable=False)
    entrenamiento_practicante = relationship(
        "MAP_PRACTICANTE", back_populates="entrenamiento")


class MAP_FUNCIONAL(Base):
    __tablename__ = 'MAP_FUNCIONAL'
    id_lider_funcional = Column(Integer, primary_key=True)
    nombre_funcional = Column(String, nullable=False)
    funcional_practicante = relationship(
        "MAP_PRACTICANTE", back_populates="funcional")


class MAP_PISO(Base):
    __tablename__ = 'MAP_PISO'
    id_piso = Column(Integer, primary_key=True, autoincrement=True)
    desc_piso = Column(String, nullable=False)
    piso_practicante = relationship("MAP_PRACTICANTE", back_populates="piso")


class MAP_ADMINISTRATIVO(Base):
    __tablename__ = "MAP_ADMINISTRATIVO"
    id_lider_administrativo = Column(
        Integer, primary_key=True, autoincrement=True)
    nombre_administrativo = Column(String, nullable=False)
    adminis_practicante = relationship(
        "MAP_PRACTICANTE", back_populates="administrativo")


class MAP_PRACTICANTE(Base):
    __tablename__ = "MAP_PRACTICANTE"
    id_practicante = Column(Integer, primary_key=True)
    codigo_practicante = Column(String, nullable=False)
    duracion_practica = Column(String, nullable=False)
    fecha_ingreso = Column(DATE, nullable=False)
    acceso_biometrico = Column(String, nullable=False)
    id_tipo_practica = Column(
        Integer, ForeignKey('MAP_TIPO_PRACTICA.id_practica'), nullable=False)
    id_institucion = Column(Integer, ForeignKey(
        'MAP_INSTITUCION.id_institucion'), nullable=False)
    id_piso = Column(Integer, ForeignKey('MAP_PISO.id_piso'), nullable=False)
    id_lider_funcional = Column(Integer, ForeignKey(
        'MAP_FUNCIONAL.id_lider_funcional'), nullable=False)
    id_lider_administrativo = Column(Integer, ForeignKey(
        'MAP_ADMINISTRATIVO.id_lider_administrativo'), nullable=False)
    id_lider_entrenamiento = Column(Integer, ForeignKey(
        'MAP_ENTRENAMIENTO.id_lider_entrenamiento'), nullable=False)
    id_usuario = Column(Integer, ForeignKey(
        'BSC_USUARIO.id_usuario'), nullable=False)
    tipo_practica = relationship(
        "MAP_TIPO_PRACTICA", back_populates="practicante")
    institucion = relationship("MAP_INSTITUCION", back_populates="institucion")
    piso = relationship("MAP_PISO", back_populates="piso_practicante")
    funcional = relationship(
        "MAP_FUNCIONAL", back_populates="funcional_practicante")
    administrativo = relationship(
        "MAP_ADMINISTRATIVO", back_populates="adminis_practicante")
    entrenamiento = relationship(
        "MAP_ENTRENAMIENTO", back_populates="entrenamiento_practicante")
    usuario = relationship("BSC_USUARIO", back_populates="practicante")


class MAP_ASISTENCIA(Base):
    __tablename__ = "MAP_ASISTENCIA"
    id_asistencia = Column(Integer, primary_key=True, autoincrement=True)
    registro = Column(DATETIME, nullable=False)
    id_practicante = Column(Integer, ForeignKey(
        'MAP_PRACTICANTE.id_practicante'), nullable=False)
    practicante = relationship("MAP_PRACTICANTE")


class MAP_HORARIO_PRACTICANTE(Base):
    __tablename__ = "MAP_HORARIO_PRACTICANTE"
    id_horario_proactante = Column(Integer, primary_key=True)
    id_practicante = Column(Integer, ForeignKey(
        MAP_PRACTICANTE.id_practicante), nullable=False)
    id_horario = Column(Integer, ForeignKey(
        'MAP_HORARIO.id_horario'), nullable=False)
    practicante = relationship("MAP_PRACTICANTE")
    horario = relationship("MAP_HORARIO")
