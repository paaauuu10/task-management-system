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

task-management-system/
├── docker-compose.yml      
├── .env.sample             
├── README.md             
└── django_backend/        
    ├── Dockerfile          
    ├── requirements.txt    
    └── scripts/
        └── entrypoint.sh   