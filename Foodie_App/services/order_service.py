from models import data_store


def place_order(data):
    if data["restaurant_id"] not in data_store.restaurants:
        return None

    order_id = data_store.order_id_counter
    data_store.order_id_counter += 1

    order = {
        "id": order_id,
        "user_id": data["user_id"],
        "restaurant_id": data["restaurant_id"],
        "dishes": data["dishes"],
        "status": "Placed"
    }

    data_store.orders[order_id] = order
    return order


def get_orders_by_restaurant(rid):
    return [o for o in data_store.orders.values() if o["restaurant_id"] == rid]


def get_orders_by_user(uid):
    return [o for o in data_store.orders.values() if o["user_id"] == uid]