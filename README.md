# Producter - Django Product Listing App

## Overview

Producter is a simple Django-based product listing application. It allows users to filter products by category and tags, perform searches, and view product details.

## Getting Started

### 1️⃣ Prerequisites

Clone the repository:

```sh
# Clone the repository
git clone https://github.com/stels17/producter.git
cd producter
```

### 2️⃣ Adjust Environment Settings (Optional)

If needed, configure your environment settings:

- Rename `.env.example` to `.env`.
- Update the environment variables with appropriate values.

### 3️⃣ Run with Docker

To build and run the application in Docker, use:

```sh
sh build_run.sh
```

The app should be available at **[http://localhost:8888/](http://localhost:8888/)**

Admin Panel is available at **/admin**, default credentials: **admin/admin123**

### 4️⃣ Run Locally

Ensure you have the following installed:

- **[Python 3.12 or newer](https://www.python.org/downloads/release/python-3120/)**
- **[Poetry](https://python-poetry.org/docs/#installation)**

Install dependencies:

```sh
poetry install
```

### 4.1 Database Setup

Run migrations to set up the database:

```sh
poetry run python manage.py migrate
```

### 4.2 Load Sample Data

To populate the database with sample products, run:

```sh
poetry run python manage.py loaddata expanded_data
```

### 4.3 Collect Static Files

Before running the server, collect all static files:

```sh
poetry run python manage.py collectstatic --noinput
```

### 4.4 Running the Development Server

Start the local development server:

```sh
poetry run python manage.py runserver 8000
```

The app should be available at **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

Admin Panel is available at **[/admin](http://127.0.0.1:8000/admin)**, default credentials: **admin/admin123**

---

## Running Tests

Run the test suite using pytest:

```sh
poetry run pytest -v -s
```

---

## AI Use Notes

AI was used to:

- Format this document
- Generate data for database population and tests
- Structure and format templates
- Help with issues along the way of coding

---

## Further Notes

- **Search**. In a real application this should be implemented using the appropriate technologies. Maybe something like [https://docs.djangoproject.com/en/5.1/ref/contrib/postgres/search/](https://docs.djangoproject.com/en/5.1/ref/contrib/postgres/search/)
- **Caching**. We can cache the products for the initial page the user sees, getting categories and tags
- Use gunicorn in the production environment as out-of-box runserver isn't suitable for that
- Implement logging
