# Django REST API with JWT Authentication

This project is a simple Django REST API that uses JWT authentication. It allows users to create, retrieve, update, and delete products.

## Endpoints

* `/products`: Get a list of all products.
* `/products/<str:category>`: Get a list of products in a specific category.
* `/products/create`: Create a new product.
* `/products/<int:pk>/update`: Update an existing product.
* `/products/<int:pk>/delete`: Delete a product.

## Authentication

The API uses JWT authentication. To authenticate, you need to provide a valid JWT token in the Authorization header.

## Example

The following code shows how to get a list of all products:


import requests

url = "https://your-api-url/products"
headers = {"Authorization": "Bearer your-jwt-token"}

response = requests.get(url, headers=headers)

if response.status_code == 200:
    products = response.json()
    print(products)


## Running the project

To run the project, you need to have Python 3 and Django installed. Once you have installed the dependencies, you can run the project by following these steps:

1. Clone the repository.
2. Create a virtual environment and activate it.
3. Install the dependencies by running `pip install -r requirements.txt`.
4. Run the development server by running `python manage.py runserver`.

The API will be available at `http://localhost:8000/`.


