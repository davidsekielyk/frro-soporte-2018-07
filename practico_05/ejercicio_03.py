from practico_05.ejercicio_01 import Base, Socio
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import sys

class DatosSocio():

    def __init__(self):
        engine = create_engine('sqlite:///base.db')
        Base.metadata.bind = engine
        DBSession = sessionmaker()
        DBSession.bind = engine
        self.session = DBSession()

        #Crear la tabla aca?
        Base.metadata.create_all(engine)

    def alta(self,socio):
        try:
            self.session.add(socio)
            self.session.commit()
            b = True
            e = False
        except:
            b=False
            e = sys.exc_info()[1]
        return b, e

    def borrar(self,viejoSocio):
        try:
            self.session.query(Socio).filter(Socio.idSoci == viejoSocio.idSoci).delete()
            self.session.commit()
            b = True
            e = False
        except:
            b = False
            e = sys.exc_info()[1]
        return b,e

    def modificar(self,modifSocio):
        try:
            self.session.query(Socio).filter(Socio.idSoci == modifSocio.idSoci).update({Socio.dni:modifSocio.dni, Socio.nombre:modifSocio.nombre, Socio.apellido:modifSocio.apellido})
            self.session.commit()
            b = True
            e = False
        except:
            b = False
            e = sys.exc_info()[1]
        return b,e

    def buscar(self,idSocio):
        soc = self.session.query(Socio).filter(Socio.idSoci == idSocio).one()
        return soc

    def todos(self):
        lp = self.session.query(Socio).all()
        return lp

    def buscarDNI(self, dni):
        cantDni = self.session.query(Socio).filter(Socio.dni == dni).count()
        return cantDni
