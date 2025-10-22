
# --- bootstrap de imports desde la raíz del proyecto ---
import sys, os
ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
# -------------------------------------------------------

from flask import Flask
from flask_cors import CORS
from infrastructure.controllers.MenuController import menu_controller
from infrastructure.database import engine
from domain.entity.Menu import Base

app = Flask(__name__)
# Enable CORS for all routes (development convenience)
CORS(app)

Base.metadata.create_all(engine)

# Registrar el controlador
app.register_blueprint(menu_controller)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)
