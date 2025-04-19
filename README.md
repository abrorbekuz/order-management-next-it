# LeadManager

To show I actually know rest-api and docker. Nobody beleives that I am Full Stack Dev.

A lead intake and tracking system built with **Django REST Framework**, designed for public submissions and internal legal team workflows. Auth, file uploads, email notifications, and a clean lead tracking flow — all in a containerized environment.

---

## ✨ Features

- 🔓 **Public Lead Form** — Anyone can submit a lead without logging in.
- 📧 **Email Notifications**:
  - Confirmation email to the prospect.
  - Notification email to the attorney (defined via environment variables).
- 🔐 **Internal Dashboard** (authentication required):
  - View all leads and detailed lead information.
  - Update the lead status (`PENDING` ➝ `REACHED_OUT`).
- 📎 File upload support (resumes/CVs).
- 🐳 Dockerized for easy local development and production deployment.
- 🔑 Token and session-based authentication using DRF's built-in system.

---

## 📋 Table of Contents

- [Tech Stack](#-tech-stack)
- [API Endpoints](#-api-endpoints)
- [Docker Setup](#-docker-setup)
- [Email Configuration](#-email-configuration)
- [Authentication](#-authentication)
- [Lead Lifecycle](#-lead-lifecycle)
- [Admin Panel](#-admin-panel)
- [File Uploads](#-file-uploads)
- [Local Dev Tips](#-local-dev-tips)
- [Production Notes](#-production-notes)
- [Project Structure](#-project-structure)
- [License](#-license)

---

## 🛠 Tech Stack

- Python 3.10
- Django 4.x
- Django REST Framework
- PostgreSQL
- Docker + Docker Compose
- Gunicorn

---

## 🧪 API Endpoints

| Method | Endpoint                          | Auth | Description                     |
|--------|-----------------------------------|------|---------------------------------|
| POST   | `/api/leads/`                     | ❌   | Submit a new lead               |
| GET    | `/api/leads/`                     | ✅   | List all leads                  |
| GET    | `/api/leads/{id}/`                | ✅   | View lead detail                |
| PATCH  | `/api/leads/{id}/update_status/`  | ✅   | Update status to `REACHED_OUT`  |

---

## 🐳 Docker Setup

### 1. Clone the repository

```bash
git clone https://github.com/yourusername/leadmanager.git
cd leadmanager
```

### 2. Set up the environment

Create a `.env` file using the provided `.env.example`:

```env
# .env
SECRET_KEY=your-django-secret
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
SMTP_EMAIL=youremail@gmail.com
SMTP_PASSWORD=your-gmail-app-password
ATTORNEY_EMAIL=attorney@example.com
```

> 📝 Use a Gmail **App Password**, not your real Gmail password.

### 3. Build and run the containers

```bash
docker-compose up --build
```

The application will be available at [http://localhost:8000](http://localhost:8000)

---

## 📤 Email Configuration

Set the following variables in your `.env` file:

```env
SMTP_EMAIL=youremail@gmail.com
SMTP_PASSWORD=your-gmail-app-password
ATTORNEY_EMAIL=attorney@example.com
```

Emails sent:

- Confirmation to the lead
- Notification to the internal attorney

To test emails in development, override the backend in `settings.py`:

```python
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"
```

---

## ✅ Authentication

Internal endpoints are secured with **Django REST Framework's default auth system**, including:

- Token Authentication
- Session Authentication

Login is required to:

- List leads
- View lead details
- Update lead status

### Login via Admin Panel

Create a superuser:

```bash
docker-compose exec web python manage.py createsuperuser
```

Access the admin UI at: [http://localhost:8000/admin](http://localhost:8000/admin)

---

## 🔁 Lead Lifecycle

```text
NEW (submitted via public form)
  ↓
PENDING (default internal state)
  ↓
REACHED_OUT (updated by internal user)
```

---

## 📁 File Uploads

Uploaded resumes are saved to:

```
/media/resumes/
```

Locally accessible at: [http://localhost:8000/media/](http://localhost:8000/media/)

---

## 🧠 Local Dev Tips

- Use the DRF login at `/api-auth/login/` for testing auth with cookies.
- Use Postman or curl for token-based auth headers.
- Resume uploads accepted as `multipart/form-data`.

---

## 🔐 Production Notes

- Set `DEBUG=False`
- Use a secure `SECRET_KEY`
- Configure allowed hosts properly
- Use HTTPS (Nginx + SSL recommended)
- Serve with Gunicorn + Nginx

---

## 📂 Project Structure

```
leadmanager/
├── apps/
│   └── lead/
│       ├── models.py
│       ├── serializers.py
│       ├── views.py
│       ├── permissions.py
│       └── email_utils.py
├── media/
├── static/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```
