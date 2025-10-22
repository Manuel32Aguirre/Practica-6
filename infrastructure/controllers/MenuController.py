from flask import Blueprint, jsonify, request
from application.impl.MenuServicioImpl import MenuServicioImpl

menu_controller = Blueprint("menu_controller", __name__)
service = MenuServicioImpl()

@menu_controller.route("/api/menu", methods=["GET"])
def listar_menu():
    menus = service.listar()
    return jsonify([
        {
            "id": m.id,
            "nombre": m.nombre,
            "costo": m.costo,
            "precio": m.precio,
            "tipo": m.tipo,
            "ingredientes": m.ingredientes,
            "url_imagen": m.url_imagen,
        }
        for m in menus
    ])

@menu_controller.route("/api/menu/<int:id>", methods=["GET"])
def obtener_menu(id):
    menu = service.obtener_por_id(id)
    if not menu:
        return jsonify({"error": "No encontrado"}), 404
    return jsonify({
        "id": menu.id,
        "nombre": menu.nombre,
        "costo": menu.costo,
        "precio": menu.precio,
        "tipo": menu.tipo,
        "ingredientes": menu.ingredientes,
        "url_imagen": menu.url_imagen,
    })

@menu_controller.route("/api/menu", methods=["POST"])
def crear_menu():
    data = request.json
    nuevo_menu = service.crear(data)
    return jsonify({
        "id": nuevo_menu.id,
        "nombre": nuevo_menu.nombre,
        "precio": nuevo_menu.precio
    }), 201

@menu_controller.route("/api/menu/<int:id>", methods=["DELETE"])
def eliminar_menu(id):
    eliminado = service.eliminar(id)
    if eliminado:
        return jsonify({"mensaje": "Eliminado correctamente"})
    return jsonify({"error": "No encontrado"}), 404
