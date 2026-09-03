from flask import Flask, jsonify

app = Flask(__name__)

users = [
    {"id": 1, "name": "Muskan", "email": "muskan@example.com"},
    {"id": 2, "name": "Rahul", "email": "rahul@example.com"}
]

@app.route("/")
def home():
    return "REST API is running!"

@app.route("/users", methods=["GET"])
def get_users():
    return jsonify(users)

if __name__ == "__main__":
    app.run(debug=True)