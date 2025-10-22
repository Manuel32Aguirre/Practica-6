from abc import ABC, abstractmethod

class MenuRepository(ABC):
    """Interfaz base para el repositorio (equivalente a JpaRepository en Java)."""

    @abstractmethod
    def find_all(self):
        pass

    @abstractmethod
    def find_by_id(self, id: int):
        pass

    @abstractmethod
    def save(self, menu):
        pass

    @abstractmethod
    def delete(self, id: int):
        pass
