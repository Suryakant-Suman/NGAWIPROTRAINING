from flask import Flask, jsonify, request

app = Flask(__name__)

# In-memory database
movies = [
    {
        "id": 101,
        "movie_name": "Interstellar",
        "language": "English",
        "duration": "2h 49m",
        "price": 250
    }
]

bookings = []

# GET all movies
@app.route("/api/movies", methods=["GET"])
def get_movies():
    return jsonify(movies), 200

# GET movie by ID
@app.route("/api/movies/<int:movie_id>", methods=["GET"])
def get_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404

# POST add movie
@app.route("/api/movies", methods=["POST"])
def add_movie():
    data = request.json
    movies.append(data)
    return jsonify(data), 201

# PUT update movie
@app.route("/api/movies/<int:movie_id>", methods=["PUT"])
def update_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            movie.update(request.json)
            return jsonify(movie), 200
    return jsonify({"error": "Movie not found"}), 404

# DELETE movie
@app.route("/api/movies/<int:movie_id>", methods=["DELETE"])
def delete_movie(movie_id):
    for movie in movies:
        if movie["id"] == movie_id:
            movies.remove(movie)
            return jsonify({"message": "Movie deleted"}), 200
    return jsonify({"error": "Movie not found"}), 404

# POST book tickets
@app.route("/api/bookings", methods=["POST"])
def book_tickets():
    data = request.json
    movie_id = data.get("movie_id")
    seats = data.get("seats")

    for movie in movies:
        if movie["id"] == movie_id:
            booking = {
                "movie_id": movie_id,
                "seats": seats,
                "total_price": movie["price"] * seats
            }
            bookings.append(booking)
            return jsonify(booking), 201

    return jsonify({"error": "Booking failed. Movie not found"}), 400

if __name__ == "__main__":
    app.run(debug=True)
