from flask import Blueprint, request, jsonify
from services import restaurant_service

restaurant_bp = Blueprint("restaurant", __name__)


@restaurant_bp.route("/api/v1/restaurants", methods=["POST"])
def register():
    restaurant, error = restaurant_service.register_restaurant(request.json)
    if error:
        return jsonify({"error": error}), 409
    return jsonify(restaurant), 201


@restaurant_bp.route("/api/v1/restaurants/<int:rid>", methods=["GET"])
def view_restaurant(rid):
    restaurant = restaurant_service.get_restaurant(rid)
    if not restaurant:
        return jsonify({"error": "Not Found"}), 404
    return jsonify(restaurant)


@restaurant_bp.route("/api/v1/restaurants/<int:rid>", methods=["PUT"])
def update_restaurant(rid):
    restaurant = restaurant_service.update_restaurant(rid, request.json)
    if not restaurant:
        return jsonify({"error": "Not Found"}), 404
    return jsonify(restaurant)


@restaurant_bp.route("/api/v1/restaurants/<int:rid>/disable", methods=["PUT"])
def disable_restaurant(rid):
    if not restaurant_service.disable_restaurant(rid):
        return jsonify({"error": "Not Found"}), 404
    return jsonify({"message": "Restaurant disabled"})