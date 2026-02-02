import requests

def test_book_tickets(base_url):
    booking = {
        "movie_id": 101,
        "seats": 3
    }
    response = requests.post(f"{base_url}/api/bookings", json=booking)
    assert response.status_code == 201
    assert response.json()["total_price"] == 750
