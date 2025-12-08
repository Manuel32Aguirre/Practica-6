from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import socket
import logging
import os  # <--- IMPORTANTE: Necesario para leer de Azure

# Configuración del logger
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# --- AQUÍ ESTÁ LA MAGIA ---
# Intentamos leer las variables de entorno (Azure).
# Si no existen, usamos los valores de tu PC ("manuel", "1234", etc.) como respaldo.
DB_USER = os.getenv("DB_USER", "manuel")
DB_PASSWORD = os.getenv("DB_PASS", "1234")  # Ojo: En Azure pusimos DB_PASS
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
DB_PORT = int(os.getenv("DB_PORT", 3306))   # Puerto estándar de MySQL es 3306
DB_NAME = os.getenv("DB_NAME", "menu_db")

# Construimos la URL con los datos que obtuvimos
MYSQL_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# Función para verificar si el puerto está abierto
def _host_open(host, port, timeout=0.5):
    try:
        with socket.create_connection((host, port), timeout=timeout):
            return True
    except Exception:
        return False

# Lógica de conexión
# Si estamos en Azure (DB_HOST no es localhost), asumimos que queremos MySQL.
if DB_HOST != "127.0.0.1" and "azure" in DB_HOST:
     logger.info("Detectado entorno Azure: Conectando a %s", DB_HOST)
     engine = create_engine(MYSQL_URL, echo=True, pool_recycle=3600)

# Si estamos en local, probamos si MySQL está prendido
elif _host_open(DB_HOST, DB_PORT):
    logger.info("MySQL local disponible en %s:%s", DB_HOST, DB_PORT)
    engine = create_engine(MYSQL_URL, echo=True)

# Si todo falla, usamos SQLite (solo para desarrollo local)
else:
    logger.warning("MySQL no disponible. Usando SQLite local (menu.db).")
    engine = create_engine("sqlite:///menu.db", echo=True)

SessionLocal = sessionmaker(bind=engine)

__all__ = ["engine", "SessionLocal"]