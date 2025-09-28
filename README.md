# Order Management Next IT

A Django + DRF based order management system with JWT auth, product and order management. Fully dockerized for easy setup.

---

## Features

* JWT Authentication (register, login, token refresh)
* Product CRUD (admin-only)
* Order CRUD (users and admin)
* Stock validation on order creation
* Filtering and ordering for orders
* Dockerized PostgreSQL and Django app

---

## Project Structure

```
.
├── apps
│   ├── api
│   ├── orders
│   └── products
├── config
│   ├── settings
│   ├── urls.py
│   └── wsgi.py
├── docker-compose.yml
├── Dockerfile
├── manage.py
├── requirements
└── tests
```

---

## Requirements

* Docker
* Docker Compose
* Python 3.10 (only for local dev if not using Docker)

---

## Docker Setup

### 1. Build and run containers

```bash
docker-compose up --build
```

This will start two services:

* **web**: Django app on port 8000
* **db**: PostgreSQL database on port 5432

### 2. Apply migrations and create superuser

```bash
docker-compose exec web python manage.py migrate
docker-compose exec web python manage.py createsuperuser
```

### 3. Access the app

* API Root: `http://localhost:8000/`
* Admin: `http://localhost:8000/admin/`

---

## Environment Variables

The web service uses `.prod.env`:

```
DJANGO_SETTINGS_MODULE=config.settings.prod
DATABASE_URL=postgres://postgres:postgres@db:5432/order_management
```

Make sure to create `.prod.env` file with these variables.

---

## Running Tests

Tests are located in `tests/unit/`. To run tests inside the Docker container:

```bash
docker-compose exec web pytest --disable-warnings
```

Or run tests locally if you have Python 3.10:

```bash
pip install -r requirements/dev.txt
pytest --disable-warnings
```

---

## API Endpoints

**Auth:**

* `POST /api/v1/auth/register/` — Register new user
* `POST /api/v1/auth/token/` — Obtain JWT token
* `POST /api/v1/auth/token/refresh/` — Refresh JWT token

**Products:**

* `GET /api/v1/products/` — List products (admin only)
* `POST /api/v1/products/` — Create product (admin only)
* `PATCH /api/v1/products/{id}/` — Update product (admin only)
* `DELETE /api/v1/products/{id}/` — Delete product (admin only)

**Orders:**

* `GET /api/v1/orders/` — List orders (user sees own, admin sees all)
* `POST /api/v1/orders/` — Create order
* `PATCH /api/v1/orders/{id}/` — Update order (status change by admin only)
* `DELETE /api/v1/orders/{id}/` — Delete order (user/admin permission)

---

## Notes

* Products stock is automatically decreased on order creation.
* Only admins can modify order status.
* Orders and products support filtering and ordering via query params.

contact the [@kachka_pachka](https://kachka_pachka.t.me) on telegram for production env file
