from models import data_store


def register_restaurant(data):
    global restaurant_id_counter

    for r in data_store.restaurants.values():
        if r["name"] == data["name"]:
            return None, "Restaurant already exists"

    restaurant_id = data_store.restaurant_id_counter
    data_store.restaurant_id_counter += 1

    restaurant = {
        "id": restaurant_id,
        "name": data["name"],
        "category": data["category"],
        "location": data["location"],
        "images": data.get("images", []),
        "contact": data["contact"],
        "approved": False,
        "enabled": True,
        "rating": 0
    }

    data_store.restaurants[restaurant_id] = restaurant
    return restaurant, None


def get_restaurant(rid):
    return data_store.restaurants.get(rid)


def update_restaurant(rid, data):
    restaurant = get_restaurant(rid)
    if not restaurant:
        return None
    restaurant.update(data)
    return restaurant


def disable_restaurant(rid):
    restaurant = get_restaurant(rid)
    if not restaurant:
        return False
    restaurant["enabled"] = False
    return True


def search_restaurants(name=None, location=None):
    result = []
    for r in data_store.restaurants.values():
        if name and name.lower() not in r["name"].lower():
            continue
        if location and location.lower() not in r["location"].lower():
            continue
        result.append(r)
    return result