# Task Management System

A modern task management system built with Django, PostgreSQL, and Redis, all orchestrated with Docker Compose.

## Features

- **Complete Authentication System**:
  - User registration and login
  - Customizable user profiles
  - Authentication via web interface and API
- **REST API**:
  - Endpoints for user management
  - JWT (JSON Web Token) authentication
  - Token blacklisting for secure logout
- **Modern Architecture**:
  - Containerized microservices
  - Persistent PostgreSQL database
  - Redis for cache storage and queues

## Requirements

- Docker and Docker Compose
- Git

## Quick Installation

```bash
# Clone the repository
git clone https://github.com/username/task-management-system.git
cd task-management-system

# Set up environment variables
cp .env.sample .env
# Edit .env with your preferred settings

# Start the services
docker-compose up -d
```

## Accessing Services

- **Django Application**: http://localhost:8000
- **PostgreSQL Database**: Accessible within Docker network (host: `db`, port: `5432`)
- **Redis**: Accessible within Docker network (host: `redis`, port: `6379`)
- **API endpoints**:
  - User Registration: `POST /api/auth/api/register/`
  - Login (JWT): `POST /api/auth/api-login/`
  - Logout: `POST /api/auth/api-logout/`
  - Refresh Token: `POST /api/auth/refresh/`
  - Users: `GET /api/users/`
  - Current User Profile: `GET /api/users/me/`

## Project Structure

```
task-management-system
├── README.md
├── django_backend
│   ├── Dockerfile
│   ├── config
│   │   ├── __init__.py
│   │   ├── __pycache__
│   │   │   ├── __init__.cpython-311.pyc
│   │   │   ├── settings.cpython-311.pyc
│   │   │   ├── urls.cpython-311.pyc
│   │   │   └── wsgi.cpython-311.pyc
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── manage.py
│   ├── requirements.txt
│   ├── scripts
│   │   └── entrypoint.sh
│   └── users
│       ├── __init__.py
│       ├── __pycache__
│       │   ├── __init__.cpython-311.pyc
│       │   ├── admin.cpython-311.pyc
│       │   ├── apps.cpython-311.pyc
│       │   ├── auth_urls.cpython-311.pyc
│       │   ├── models.cpython-311.pyc
│       │   ├── serializers.cpython-311.pyc
│       │   ├── urls.cpython-311.pyc
│       │   └── views.cpython-311.pyc
│       ├── admin.py
│       ├── apps.py
│       ├── auth_urls.py
│       ├── migrations
│       │   ├── 0001_initial.py
│       │   ├── __init__.py
│       │   └── __pycache__
│       │       ├── 0001_initial.cpython-311.pyc
│       │       └── __init__.cpython-311.pyc
│       ├── models.py
│       ├── serializers.py
│       ├── templates
│       │   └── users
│       │       ├── base.html
│       │       ├── login.html
│       │       ├── login_success.html
│       │       └── register.html
│       ├── tests.py
│       ├── urls.py
│       └── views.py
├── docker-compose.yml
└── docs
    └── DECISIONS.md
```

## Development

### Run Migrations

```bash
docker-compose exec web python manage.py migrate
```

### Create a Superuser

```bash
docker-compose exec web python manage.py createsuperuser
```

### Access Django Shell

```bash
docker-compose exec web python manage.py shell
```

## Technical Considerations

The project uses:

- **Django 4.2+**: Modern and secure web framework
- **Django REST Framework**: For creating the REST API
- **SimpleJWT**: For token-based authentication
- **PostgreSQL 15**: Robust relational database
- **Redis 7**: For caching and potential background tasks

For more details about technical decisions, see [docs/DECISIONS.md](docs/DECISIONS.md).

## License

[MIT](LICENSE)