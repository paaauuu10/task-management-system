FROM python:3.11-slim AS builder

WORKDIR /app/django_backend

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENTRYPOINT ["/app/django_backend/scripts/entrypoint.sh"]