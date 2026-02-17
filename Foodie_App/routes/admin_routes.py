from flask import Blueprint, jsonify
from models import data_store

admin_bp = Blueprint("admin", __name__)


@admin_bp.route("/api/v1/admin/restaurants/<int:rid>/approve", methods=["PUT"])
def approve(rid):
    r = data_store.restaurants.get(rid)
    if not r:
        return jsonify({"error": "Not Found"}), 404
    r["approved"] = True
    return jsonify({"message": "Approved"})


@admin_bp.route("/api/v1/admin/restaurants/<int:rid>/disable", methods=["PUT"])
def disable(rid):
    r = data_store.restaurants.get(rid)
    if not r:
        return jsonify({"error": "Not Found"}), 404
    r["enabled"] = False
    return jsonify({"message": "Disabled"})


@admin_bp.route("/api/v1/admin/feedback", methods=["GET"])
def feedback():
    return jsonify(data_store.feedback)


@admin_bp.route("/api/v1/admin/orders", methods=["GET"])
def view_orders():
    return jsonify(list(data_store.orders.values()))