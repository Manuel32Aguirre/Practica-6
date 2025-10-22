from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DB_USER = "manuel"
DB_PASSWORD = "1234"
DB_HOST = "127.0.0.1"
DB_PORT = "3309"
DB_NAME = "menu_db"

try:
    DATABASE_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
    engine = create_engine(DATABASE_URL, echo=True)
    engine.connect()
    print(f"MySQL conectado a la base '{DB_NAME}' ✅")
except Exception as e:
    print(f"MySQL at {DB_NAME} not available. Falling back to SQLite.")
    print("Detalle:", e)
    DATABASE_URL = "sqlite:///menu.db"
    engine = create_engine(DATABASE_URL, echo=True)

SessionLocal = sessionmaker(bind=engine)
