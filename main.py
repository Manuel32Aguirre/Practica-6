# --- bootstrap de imports desde la raíz del proyecto ---
import sys, os
ROOT = os.path.dirname(os.path.abspath(__file__))
if ROOT not in sys.path:
    sys.path.insert(0, ROOT)
# -------------------------------------------------------

# AGREGA AQUÍ send_from_directory
from flask import Flask, send_from_directory
from flask_cors import CORS
from infrastructure.controllers.MenuController import menu_controller
from infrastructure.database import engine
from domain.entity.Menu import Base

app = Flask(__name__)
# Enable CORS for all routes (development convenience)
CORS(app)

# OJO: Esto conectará a la base de datos al arrancar.
# Asegúrate de tener las variables de entorno configuradas en Azure.
Base.metadata.create_all(engine)

# Registrar el controlador
app.register_blueprint(menu_controller)

# --- NUEVA RUTA: Sirve el archivo ui.html en la raíz ---
@app.route('/')
def home():
    # Busca el archivo ui.html en la carpeta actual (.) y lo muestra
    return send_from_directory('.', 'ui.html')
# -------------------------------------------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080, debug=True)