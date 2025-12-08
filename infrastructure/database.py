from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os
import logging

# Configuración básica
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Leemos las variables
DB_USER = os.getenv("DB_USER", "manuel")
DB_PASSWORD = os.getenv("DB_PASS", "1234")
DB_HOST = os.getenv("DB_HOST", "127.0.0.1")
# Forzamos que sea entero
DB_PORT = int(os.getenv("DB_PORT", 3306))
DB_NAME = os.getenv("DB_NAME", "menu_db")

# Construimos la URL
MYSQL_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# --- CAMBIO IMPORTANTE: SIN RED DE SEGURIDAD ---
# Intentamos conectar directo. Si falla, que lance el error para verlo.
logger.info(f"Intentando conectar a: {DB_HOST}:{DB_PORT}...")

# Agregamos ssl_args para Azure (a veces es estricto con SSL)
connect_args = {}
if "azure" in DB_HOST:
    connect_args = {"ssl": {"fake_flag_to_enable": True}} 
    # Nota: pymysql usa SSL por defecto si está disponible, 
    # pero a veces necesita un empujoncito.

engine = create_engine(
    MYSQL_URL, 
    echo=True, 
    pool_recycle=3600,
    connect_args=connect_args
)

SessionLocal = sessionmaker(bind=engine)

__all__ = ["engine", "SessionLocal"]