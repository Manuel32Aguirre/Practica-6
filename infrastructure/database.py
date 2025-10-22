"""Compatibility shim: export engine and SessionLocal from controllers.database

This file keeps existing imports working (some modules import
`infrastructure.database` while implementation lives under
`infrastructure/controllers/database.py`).
"""

from .controllers.database import engine, SessionLocal

__all__ = ["engine", "SessionLocal"]
"""Database engine and session factory for the project.

This module centralizes the database configuration. It will try to
use MySQL when available and fall back to a local SQLite file
(`menu.db`) for development convenience.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import socket
import logging

DB_USER = "manuel"
DB_PASSWORD = "1234"
DB_HOST = "127.0.0.1"
DB_PORT = 3309
DB_NAME = "menu_db"

logger = logging.getLogger(__name__)

def _host_open(host, port, timeout=0.5):
	try:
		with socket.create_connection((host, port), timeout=timeout):
			return True
	except Exception:
		return False

MYSQL_URL = f"mysql+pymysql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

if _host_open(DB_HOST, DB_PORT):
	logger.info("MySQL appears available at %s:%s — using MySQL", DB_HOST, DB_PORT)
	engine = create_engine(MYSQL_URL, echo=True)
else:
	logger.warning("MySQL at %s:%s not reachable — falling back to SQLite.", DB_HOST, DB_PORT)
	engine = create_engine("sqlite:///menu.db", echo=True)

SessionLocal = sessionmaker(bind=engine)

__all__ = ["engine", "SessionLocal"]
