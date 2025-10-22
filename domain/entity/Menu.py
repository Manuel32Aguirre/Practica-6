from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Menu(Base):
    __tablename__ = "menu"

    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(100), nullable=False)
    costo = Column(Float, nullable=False)
    precio = Column(Float, nullable=False)
    tipo = Column(String(50), nullable=False)
    ingredientes = Column(String(255))
    url_imagen = Column(String(255))

    def __init__(self, nombre, costo, precio, tipo, ingredientes=None, url_imagen=None):
        self.nombre = nombre
        self.costo = costo
        self.precio = precio
        self.tipo = tipo
        self.ingredientes = ingredientes
        self.url_imagen = url_imagen

    def __repr__(self):
        return f"<Menu(id={self.id}, nombre='{self.nombre}', tipo='{self.tipo}', precio={self.precio})>"
