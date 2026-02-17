from models import data_store


def add_dish(restaurant_id, data):
    if restaurant_id not in data_store.restaurants:
        return None

    dish_id = data_store.dish_id_counter
    data_store.dish_id_counter += 1

    dish = {
        "id": dish_id,
        "restaurant_id": restaurant_id,
        "name": data["name"],
        "type": data["type"],
        "price": data["price"],
        "available_time": data["available_time"],
        "image": data.get("image"),
        "enabled": True
    }

    data_store.dishes[dish_id] = dish
    return dish


def update_dish(dish_id, data):
    dish = data_store.dishes.get(dish_id)
    if not dish:
        return None
    dish.update(data)
    return dish


def delete_dish(dish_id):
    return data_store.dishes.pop(dish_id, None)


def update_status(dish_id, status):
    dish = data_store.dishes.get(dish_id)
    if not dish:
        return False
    dish["enabled"] = status
    return True