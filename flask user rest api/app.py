from flask import Flask, jsonify, request

app = Flask(__name__)

users = [
    {"id": 1, "name": "Muskan", "email": "muskan@example.com"},
    {"id": 2, "name": "Rahul", "email": "rahul@example.com"}
]


@app.route("/")
def home():
    return "REST API is running!"


# GET - Get all users
@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)


# POST - Add a new user
@app.route("/users", methods=["POST"])
def add_user():
    data = request.get_json()

    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "email": data["email"]
    }

    users.append(new_user)

    return jsonify(new_user), 201


# PUT - Update a user
@app.route("/users/<int:user_id>", methods=["PUT"])
def update_user(user_id):
    data = request.get_json()

    for user in users:
        if user["id"] == user_id:
            user["name"] = data["name"]
            user["email"] = data["email"]

            return jsonify(user)

    return jsonify({"message": "User not found"}), 404


# DELETE - Delete a user
@app.route("/users/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):

    for user in users:
        if user["id"] == user_id:
            users.remove(user)

            return jsonify({
                "message": "User deleted successfully"
            })

    return jsonify({"message": "User not found"}), 404


if __name__ == "__main__":
    app.run(debug=True)

