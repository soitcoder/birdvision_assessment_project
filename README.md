# Product API

This is a Flask-based RESTful API for managing a product inventory. It provides endpoints for user authentication, product management, and other related tasks.

## Table of Contents

- [Setup and Running Instructions](#setup-and-running-instructions)
- [API Endpoints](#api-endpoints)
    - [Login](#login)
    - [Signup](#signup)
    - [Products](#products)
        - [Get All Products](#get-all-products)
        - [Get Product by ID](#get-product-by-id)
        - [Create a Product](#create-a-product)
        - [Update a Product](#update-a-product)
        - [Delete a Product](#delete-a-product)

## Setup and Running Instructions

1. **Prerequisites**:
    - Python 3.11 or higher
    - A virtual environment (recommended)
    - Required Python packages (listed in `requirements.txt`)

2. **Installation**:
    - Clone the repository:

    ```shell
    git clone https://github.com/yourusername/product-api.git
    cd product-api
    ```

    - Install the required packages:

    ```shell
    pip install -r requirements.txt
    ```

3. **Database Initialization**:
    - Ensure that the database file (`products.db`) is accessible.
    - Create the database schema:

    ```shell
    python create_db.py  # Optional script to create initial database schema
    ```

4. **Running the Application**:
    - Start the Flask application:

    ```shell
    python app.py
    ```

    The application will run on `http://localhost:5000`.

## API Endpoints

### Login

- **URL**: `/login`
- **Method**: `POST`
- **Request**:
    - JSON body with the following fields:
        - `username` (string): The username of the user.
        - `password` (string): The password of the user.
- **Response**:
    - JSON object containing an access token:
        ```json
        {
            "access_token": "your_access_token"
        }
        ```

- **Example**:
    ```shell
    curl -X POST http://localhost:5000/login \
        -H "Content-Type: application/json" \
        -d '{"username": "user", "password": "pass"}'
    ```

### Signup

- **URL**: `/signup`
- **Method**: `POST`
- **Request**:
    - JSON body with the following fields:
        - `username` (string): The username of the new user.
        - `password` (string): The password of the new user.
- **Response**:
    - JSON object containing the user data:
        ```json
        {
            "id": 1,
            "username": "newuser",
            "password": "hashed_password"
        }
        ```

- **Example**:
    ```shell
    curl -X POST http://localhost:5000/signup \
        -H "Content-Type: application/json" \
        -d '{"username": "newuser", "password": "newpass"}'
    ```

### Products

#### Get All Products

- **URL**: `/products`
- **Method**: `GET`
- **Request**:
    - No request body required, but authorization header is required:
        - `Authorization: Bearer <access_token>`
- **Response**:
    - JSON array of product objects:
        ```json
        [
            {
                "id": 1,
                "title": "Product 1",
                "description": "Product 1 description",
                "price": 10.99
            },
            {
                "id": 2,
                "title": "Product 2",
                "description": "Product 2 description",
                "price": 15.49
            }
        ]
        ```

- **Example**:
    ```shell
    curl -X GET http://localhost:5000/products \
        -H "Authorization: Bearer <your_access_token>"
    ```

#### Get Product by ID

- **URL**: `/products/<int:product_id>`
- **Method**: `GET`
- **Request**:
    - No request body required, but authorization header is required:
        - `Authorization: Bearer <access_token>`
- **Response**:
    - JSON object containing the product data:
        ```json
        {
            "id": 1,
            "title": "Product 1",
            "description": "Product 1 description",
            "price": 10.99
        }
        ```

- **Example**:
    ```shell
    curl -X GET http://localhost:5000/products/1 \
        -H "Authorization: Bearer <your_access_token>"
    ```

#### Create a Product

- **URL**: `/products`
- **Method**: `POST`
- **Request**:
    - JSON body with the following fields:
        - `title` (string): The title of the product.
        - `description` (string): The description of the product.
        - `price` (float): The price of the product.
    - Authorization header required:
        - `Authorization: Bearer <access_token>`
- **Response**:
    - JSON object containing the created product data:
        ```json
        {
            "id": 1,
            "title": "Product 1",
            "description": "Product 1 description",
            "price": 10.99
        }
        ```

- **Example**:
    ```shell
    curl -X POST http://localhost:5000/products \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer <your_access_token>" \
        -d '{"title": "Product 1", "description": "Product 1 description", "price": 10.99}'
    ```

#### Update a Product

- **URL**: `/products/<int:product_id>`
- **Method**: `PUT`
- **Request**:
    - JSON body with any fields to update:
        - `title` (string): The title of the product.
        - `description` (string): The description of the product.
        - `price` (float): The price of the product.
    - Authorization header required:
        - `Authorization: Bearer <access_token>`
- **Response**:
    - JSON object containing the updated product data:
        ```json
        {
            "id": 1,
            "title": "Product 1 Updated",
            "description": "Product 1 description updated",
            "price": 12.99
        }
        ```

- **Example**:
    ```shell
    curl -X PUT http://localhost:5000/products/1 \
        -H "Content-Type: application/json" \
        -H "Authorization: Bearer <your_access_token>" \
        -d '{"title": "Product 1 Updated", "description": "Product 1 description updated", "price": 12.99}'
    ```

#### Delete a Product

- **URL**: `/products/<int:product_id>`
- **Method**: `DELETE`
- **Request**:
    - No request body required, but authorization header is required:
        - `Authorization: Bearer <access_token>`
- **Response**:
    - Empty JSON object with HTTP status code `204` (No Content).

- **Example**:
    ```shell
    curl -X DELETE http://localhost:5000/products/1 \
        -H "Authorization: Bearer <your_access_token>"
    ```
