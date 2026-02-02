import requests

def test_get_movies(base_url):
    response = requests.get(f"{base_url}/api/movies")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_add_movie(base_url):
    movie = {
        "id": 103,
        "movie_name": "Avatar",
        "language": "English",
        "duration": "2h 42m",
        "price": 280
    }
    response = requests.post(f"{base_url}/api/movies", json=movie)
    assert response.status_code == 201
    assert response.json()["movie_name"] == "Avatar"
