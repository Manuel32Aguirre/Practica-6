from application.MenuServicio import MenuServicio
from domain.entity.Menu import Menu
from infrastructure.database import SessionLocal

class MenuServicioImpl(MenuServicio):
    """Implementación del servicio (equivalente a @Service en Spring)."""

    def listar(self):
        session = SessionLocal()
        try:
            return session.query(Menu).all()
        finally:
            session.close()

    def obtener_por_id(self, id: int):
        session = SessionLocal()
        try:
            return session.query(Menu).filter(Menu.id == id).first()
        finally:
            session.close()

    def crear(self, menu_data: dict):
        session = SessionLocal()
        try:
            nuevo_menu = Menu(
                nombre=menu_data["nombre"],
                costo=menu_data["costo"],
                precio=menu_data["precio"],
                tipo=menu_data["tipo"],
                ingredientes=menu_data.get("ingredientes"),
                url_imagen=menu_data.get("url_imagen"),
            )
            session.add(nuevo_menu)
            session.commit()
            session.refresh(nuevo_menu)
            return nuevo_menu
        finally:
            session.close()

    def eliminar(self, id: int):
        session = SessionLocal()
        try:
            menu = session.query(Menu).filter(Menu.id == id).first()
            if menu:
                session.delete(menu)
                session.commit()
                return True
            return False
        finally:
            session.close()
