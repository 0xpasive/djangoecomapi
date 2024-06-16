# Django E-commerce API

A Django-based RESTful API for managing an e-commerce platform, allowing CRUD operations for products, categories, carts, cart items, and orders. 

## Features

- CRUD operations for Categories, Products, Carts, Cart Items, and Orders.
- User authentication and management.


## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/yourusername/django-ecommerce-api.git
    cd django-ecommerce-api
    ```

2. **Create and activate a virtual environment:**

    ```sh
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

4. **Apply migrations:**

    ```sh
    python manage.py makemigrations
    python manage.py migrate
    ```

5. **Create a superuser:**

    ```sh
    python manage.py createsuperuser
    ```

6. **Run the development server:**

    ```sh
    python manage.py runserver
    ```
# API Endpoints
The API includes the following endpoints:

## Categories
- GET /api/category/ - List all categories
- POST /api/category/ - Create a new category
- GET /api/category/{id}/ - Retrieve a specific category
- PUT /api/category/{id}/ - Update a specific category
- DELETE /api/category/{id}/ - Delete a specific category

## Products
- GET /api/product/ - List all products
- POST /api/product/ - Create a new product
- GET /api/product/{id}/ - Retrieve a specific product
- PUT /api/product/{id}/ - Update a specific product
- DELETE /api/product/{id}/ - Delete a specific product

## Carts
- GET /api/cart/ - List all carts
- POST /api/cart/ - Create a new cart
- GET /api/cart/{id}/ - Retrieve a specific cart
- PUT /api/cart/{id}/ - Update a specific cart
- DELETE /api/cart/{id}/ - Delete a specific cart

## Cart Items
- GET /api/cartitem/ - List all cart items
- POST /api/cartitem/ - Create a new cart item
- GET /api/cartitem/{id}/ - Retrieve a specific cart item
- PUT /api/cartitem/{id}/ - Update a specific cart item
- DELETE /api/cartitem/{id}/ - Delete a specific cart item

## Orders
- GET /api/order/ - List all orders
- POST /api/order/ - Create a new order
- GET /api/order/{id}/ - Retrieve a specific order
- PUT /api/order/{id}/ - Update a specific order
- DELETE /api/order/{id}/ - Delete a specific order

## Users
- GET /api/user/ - List all users
- POST /api/user/ - Create a new user
- GET /api/user/{id}/ - Retrieve a specific user
- PUT /api/user/{id}/ - Update a specific user
- DELETE /api/user/{id}/ - Delete a specific user

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Contributing
- Fork the repository.
- Create your feature branch (git checkout -b feature/your-feature).
- Commit your changes (git commit -m 'Add some feature').
- Push to the branch (git push origin feature/your-feature).
- Open a pull request.


