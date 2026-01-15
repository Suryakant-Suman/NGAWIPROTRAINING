import json

data = {
    "name": "ravi",
    "age": 20,
    "height": "1.5m",
    "weight": 75,
}
with open("data.json", "w") as file:
    json.dump(data, file)