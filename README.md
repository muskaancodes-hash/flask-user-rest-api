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
## Part 3 — POST

Implemented a POST `/users` endpoint to add new users.

The API accepts user details in JSON format and adds the new user to the users list.

### POST /users

Example request:

```json
{
## Part 4 — PUT

Implemented a PUT `/users/<id>` endpoint to update an existing user's information.

### PUT /users/1

Example request:

```json
{
    "name": "Aman Sharma",
    "email": "aman.sharma@example.com"
}

    "name": "Aman",
    "email": "aman@example.com"
}
## Part 5 — DELETE

Implemented a DELETE `/users/<id>` endpoint to delete an existing user.

### DELETE /users/1

The API removes the specified user and returns a success message.

If the user does not exist, the API returns a `404 Not Found` response.

