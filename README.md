# flask-user-rest-api
A simple REST API built with Flask to manage user data using GET, POST, PUT, and DELETE requ

## Part 1
Created a basic Flask application with a home endpoint.

## Technologies Used
- Python
- Flask

## Part 2

Added an in-memory list to store user data.

Implemented a GET `/users` endpoint to retrieve all users in JSON format.

### GET /users

Returns a list of all users.

Example response:

```json
[
    {
        "id": 1,
        "name": "Muskan",
        "email": "muskan@example.com"
    },
    {
        "id": 2,
        "name": "Rahul",
        "email": "rahul@example.com"
    }
]
