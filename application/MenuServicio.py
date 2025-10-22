from abc import ABC, abstractmethod

class MenuServicio(ABC):
    """Interfaz del servicio de aplicación (equivalente a la interfaz @Service en Java)."""

    @abstractmethod
    def listar(self):
        pass

    @abstractmethod
    def obtener_por_id(self, id: int):
        pass

    @abstractmethod
    def crear(self, menu_data: dict):
        pass

    @abstractmethod
    def eliminar(self, id: int):
        pass
