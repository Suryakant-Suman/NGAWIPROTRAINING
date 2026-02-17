from flask import Blueprint, jsonify
from services import order_service

order_bp = Blueprint("order", __name__)


@order_bp.route("/api/v1/restaurants/<int:rid>/orders", methods=["GET"])
def restaurant_orders(rid):
    return jsonify(order_service.get_orders_by_restaurant(rid))


@order_bp.route("/api/v1/users/<int:uid>/orders", methods=["GET"])
def user_orders(uid):
    return jsonify(order_service.get_orders_by_user(uid))