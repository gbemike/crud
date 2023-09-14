
Person Management API Documentation

Overview

This API allows you to manage a collection of persons. It supports basic CRUD (Create, Read, Update, Delete) operations for persons. You can create, retrieve, update, and delete person records.

 Base URL

The base URL for all API endpoints is `http://your-server.com/`. Replace `your-server.com` with the actual URL or IP address of your server.

Endpoints

1. Retrieve All Persons

- HTTP Method: GET
- URL:** `/api`
- Description: Retrieve a list of all persons.
- Response:

    ```json
    [
        {
            "id": 1,
            "username": "JohnDoe",
            "track": "Backend"
        },
        {
            "id": 2,
            "username": "JaneSmith",
            "track": "Frontend"
        }
        // ... (other person records)
    ]
    ```

2. Create a New Person

- HTTP Method:POST
- URL:’/api`
- Description: Create a new person.
- Request:

    ```json
    {
        "username": "NewUser",
        "track": "DevOps"
    }
    ```

- Response:

    ```json
    {
        "id": 3,
        "username": "NewUser",
        "track": "DevOps"
    }
    ```

3. Retrieve a Specific Person

- HTTP Method:GET
- URL: `/api/{id}`
- Description: Retrieve details of a specific person by their ID.
- Response:

    ```json
    {
        "id": 1,
        "username": "JohnDoe",
        "track": "Backend"
    }
    ```

4. Update a Specific Person

- HTTP Method: PUT
- URL:`/api/{id}`
- Description: Update details of a specific person by their ID.
- Request:

    ```json
    {
        "username": "UpdatedUser",
        "track": "Data Science"
    }
    ```

- Response:

    ```json
    {
        "message": "Success"
    }
    ```

5. Delete a Specific Person

- HTTP Method:DELETE
- URL: `/api/{id}`
- Description: Delete a specific person by their ID.
- Response:

    ```json
    {
        "message": "Deleted Successfully"
    }
    ```

 Example Usage

Here's how you can use the API endpoints:

- Retrieve all persons: Send a GET request to `/api`.
- Create a new person: Send a POST request to `/api` with a JSON body containing `username` and `track`.
- Retrieve a specific person: Send a GET request to `/api/{id}` where `{id}` is the person's ID.
- Update a specific person: Send a PUT request to `/api/{id}` with a JSON body containing updated `username` and `track`.
- Delete a specific person: Send a DELETE request to `/api/{id}` where `{id}` is the person's ID.

Notes

- This API uses SQLite as its database. You can modify the database configuration in the code to use a different database system.
- Always include the appropriate request data and ensure proper authentication and authorization mechanisms in a production environment.
