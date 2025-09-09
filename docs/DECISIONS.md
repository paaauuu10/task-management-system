# Project Decisions and Reflections

## Technical Decisions

[DECISION 1]

Decision: Use python:3.11-slim as the base image.
Justification:
    · It's an official Python image, maintained by the Python/Docker teams.
    · The slim variant is significantly smaller than the full Debian-based image, reducing build times and final size.

[DECISION 2]

Decision: Use psycopg2-binary
Justification: 
    · Avoids the need for compilation or installation of additional system libraries.

## Features Implemented

1. **Complete User Authentication System**
   - Implemented both with HTML views and REST API
   - Includes registration, login, logout, and user profile
   - Justification: Authentication is fundamental for any task management system

2. **REST API Architecture**
   - Endpoints for users and authentication with JWT
   - Justification: Allows integration with any frontend and other applications

3. **Docker Containerization**
   - Docker and docker-compose to facilitate development and deployment
   - Justification: Improves reproducibility and simplifies configuration

## Features Not Implemented

1. **Task Management System**
   - Reason: Priority was given to having a solid foundation with authentication before adding specific functionalities

2. **Complete Celery Integration**
   - Reason: Although Redis is configured, background tasks were not fully implemented
   - Infrastructure is ready but specific implementations are missing

## Time Allocation

- **30%** - Initial setup (Docker, project structure, database)
- **40%** - User system and authentication implementation
- **20%** - REST API and JWT tokens
- **10%** - Frontend templates and views

## Technical Challenges

1. **JWT Integration with Django's Session System**
   - Maintaining coherence between API authentication and web session authentication

2. **Docker Configuration for Development**
   - Getting volumes to work correctly to avoid rebuilding images during development

## Trade-offs

1. **Simplicity vs. Functionality**
   - Opted for a simpler but solid implementation, instead of many underdeveloped features
   - Justification: It's better to have a system that works well for basic functionalities

2. **Django Templates vs. SPA Frontend**
   - Used Django Templates for the frontend instead of building a separate SPA
   - Justification: Time savings and simplicity in implementation

## Improvements with More Time

1. **Complete Task Management System Implementation**
   - Models for tasks, projects, tags
   - Endpoints for full CRUD operations
   - Frontend views for task management

2. **Real Celery Integration**
   - Scheduled tasks
   - Background notifications
   - Heavy calculations

3. **Unit and Integration Tests**
   - Improve test coverage

## Justification for Using Django Templates

1. **Simplicity and Speed of Implementation**
   - Allows rapid development of frontend functionality without configuring a new project

2. **Coherence with Backend**
   - Leverages Django's authentication and session system

3. **Suitable for Prototyping**
   - For a technical test, it demonstrates knowledge of both backend and basic frontend

4. **Scalable**
   - The presence of the REST API allows for later migration to a more sophisticated frontend if needed

