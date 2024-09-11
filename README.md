# My Flask API Project


## Overview

- RESTful API endpoints for managing orders, customers, and employees.
- Versioned API routes (/api/v1).
- ntegrated with PostgreSQL using SQLAlchemy.
- Database migrations handled by Flask-Migrate.


## Technologies

- Flask: Micro web framework for Python.
- Flask-RESTful: Extension for building REST APIs quickly.
- Flask-Migrate: SQLAlchemy database migrations for Flask.
- SQLAlchemy: SQL toolkit and Object-Relational Mapping (ORM) library.
- PostgreSQL: Relational database management system.


## Setup

### Prerequisites

- Python 3.8 or higher
- PostgreSQL
- Virtual environment (recommended)

### Installation

1. **Clone the repository:**

   ```bash
    git clone https://github.com/yourusername/my_flask_app.git
    cd my_flask_app
    ```

2. **Create and activate a virtual environment:**

    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. **Install the dependencies:**

    ```bash
    pip3 install -r requirements.txt
    ```

4. **Configure your environment:**

    Create a `.env` file in the root directory and add the following environment variables:

    ```txt
    FLASK_APP=app
    FLASK_ENV=development
    DATABASE_URL=postgresql://username:password@localhost/dbname
    SECRET_KEY=your-secret-key
    ```

    Replace `username`, `password`, `localhost`, `dbname`, and `your-secret-key` with your PostgreSQL credentials and a secure key for your application.

5. **Initialize the database::**

    ```bash
    flask db init
    flask db migrate -m "Initial migration."
    flask db upgrade
    ```

6. **Run the application:**

    ```bash
    flask run
    ```
    The application will be available at `http://127.0.0.1:5000`.

## API Endpoints

### Orders

- GET `/api/v1/orders/`: List all orders.
- GET `/api/v1/orders/int:order_id`: Retrieve a specific order.
- POST `/api/v1/orders/`: Create a new order.
- PUT `/api/v1/orders/int:order_id`: Update an existing order.
- DELETE `/api/v1/orders/int:order_id`: Delete an order.

### Customers
- GET `/api/v1/customers/`: List all customers.
- GET `/api/v1/customers/int:customer_id`: Retrieve a specific customer.
- POST `/api/v1/customers/`: Create a new customer.
- PUT `/api/v1/customers/int:customer_id`: Update an existing customer.
- DELETE `/api/v1/customers/int:customer_id`: Delete a customer.

### Employees
- GET `/api/v1/employees/`: List all employees.
- GET `/api/v1/employees/int:employee_id`: Retrieve a specific employee.
- POST `/api/v1/employees/`: Create a new employee.
- PUT `/api/v1/employees/int:employee_id`: Update an existing employee.
- DELETE `/api/v1/employees/int:employee_id`: Delete an employee.
