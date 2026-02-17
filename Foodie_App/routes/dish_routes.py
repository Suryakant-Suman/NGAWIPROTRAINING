from flask import Blueprint, request, jsonify
from services import dish_service

dish_bp = Blueprint("dish", __name__)


@dish_bp.route("/api/v1/restaurants/<int:rid>/dishes", methods=["POST"])
def add_dish(rid):
    dish = dish_service.add_dish(rid, request.json)
    if not dish:
        return jsonify({"error": "Restaurant not found"}), 404
    return jsonify(dish), 201


@dish_bp.route("/api/v1/dishes/<int:dish_id>", methods=["PUT"])
def update_dish(dish_id):
    dish = dish_service.update_dish(dish_id, request.json)
    if not dish:
        return jsonify({"error": "Not Found"}), 404
    return jsonify(dish)


@dish_bp.route("/api/v1/dishes/<int:dish_id>", methods=["DELETE"])
def delete_dish(dish_id):
    if not dish_service.delete_dish(dish_id):
        return jsonify({"error": "Not Found"}), 404
    return jsonify({"message": "Dish deleted"})


@dish_bp.route("/api/v1/dishes/<int:dish_id>/status", methods=["PUT"])
def update_status(dish_id):
    status = request.json.get("enabled")
    if not dish_service.update_status(dish_id, status):
        return jsonify({"error": "Not Found"}), 404
    return jsonify({"message": "Status updated"})