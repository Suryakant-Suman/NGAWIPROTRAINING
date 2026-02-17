from flask import Blueprint, request, jsonify
from models import data_store
from services import restaurant_service, order_service

user_bp = Blueprint("user", __name__)


@user_bp.route("/api/v1/users/register", methods=["POST"])
def register_user():
    data = request.json

    for u in data_store.users.values():
        if u["email"] == data["email"]:
            return jsonify({"error": "User exists"}), 409

    uid = data_store.user_id_counter
    data_store.user_id_counter += 1

    user = {"id": uid, **data}
    data_store.users[uid] = user
    return jsonify(user), 201


@user_bp.route("/api/v1/restaurants/search", methods=["GET"])
def search():
    name = request.args.get("name")
    location = request.args.get("location")
    result = restaurant_service.search_restaurants(name, location)
    return jsonify(result)


@user_bp.route("/api/v1/orders", methods=["POST"])
def place_order():
    order = order_service.place_order(request.json)
    if not order:
        return jsonify({"error": "Invalid data"}), 400
    return jsonify(order), 201


@user_bp.route("/api/v1/ratings", methods=["POST"])
def give_rating():
    data_store.ratings.append(request.json)
    return jsonify(request.json), 201