# Producter - Django Product Listing App

## Overview

Producter is a simple Django-based product listing application. It allows users to filter products by category and tags, perform searches, and view product details.

## Getting Started

### 1️⃣ Prerequisites

Ensure you have the following installed:

- [Python 3.10 or newer](https://www.python.org/downloads/release/python-3100/)
- [Poetry](https://python-poetry.org/docs/#installation)

### 2️⃣ Installation

Clone the repository and install dependencies using Poetry:

```sh
# Clone the repository
git clone https://github.com/yourusername/producter.git
cd producter

# Install dependencies
poetry install
```

### 3️⃣ Adjust Environment Settings (Optional)

If needed, configure your environment settings:

- Rename `.env.example` to `.env`.
- Update the environment variables with appropriate values.

### 4️⃣ Database Setup

Run migrations to set up the database:

```sh
poetry run python manage.py migrate
```

### 5️⃣ Load Sample Data

To populate the database with sample products, run:

```sh
poetry run python manage.py loaddata expanded_data
```

### 6️⃣ Running the Development Server

Start the local development server:

```sh
poetry run python manage.py runserver
```

The app will be available at **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**.

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

- Search. In a real application this should be implemented using the appropriate technologies. Maybe something like [https://docs.djangoproject.com/en/5.1/ref/contrib/postgres/search/](https://docs.djangoproject.com/en/5.1/ref/contrib/postgres/search/)
- Caching. We can cache the products for the initial page the user sees, getting categories and tags
- Use gunicorn
- Implement logging


