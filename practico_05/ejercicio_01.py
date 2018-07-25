from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String


Base = declarative_base()

class Socio(Base):
    __tablename__ = "socios"
    idSoci = Column(Integer, primary_key=True)
    dni = Column(Integer)
    nombre = Column(String(20))
    apellido = Column(String(20))
