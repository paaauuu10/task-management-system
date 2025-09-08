# Task Management System

A test project for a technical interview.
Objective: build a task management platform using Django + PostgreSQL + Redis + Celery, all orchestrated with Docker Compose.

## Quick Start

```bash
git clone <repo>
cd task-management-system
cp .env.sample .env
docker-compose up

## Project Structure

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
│   └── scripts
│       └── entrypoint.sh
├── docker-compose.yml
└── docs
    └── DECISIONS.md

Accessing Services
Django: http://localhost:8000
PostgreSQL: accessible inside Docker network on container db, port 5432
Redis: accessible inside Docker network on container redis, port 6379