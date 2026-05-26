# task-management-api
Task management backend API using FastAPI and SQL.

## Goal
Practice backend development, REST API design, and SQL database integration using FastAPI.

## Features
- User authentication
- Task creation and management
- CRUD operations
- Database integration
- Request validation

## Tech Stack
- Python
- FastAPI
- SQL
- SQLite

## Status
Work in progress.
## Installation

1. Clone the repository

```bash
git clone https://github.com/Aggeliki-polychronaki/task-management-api.git 

 ## Run the API

```bash
uvicorn main:app --reload  

 
και μετά:

```md
## Available Endpoints

- GET /tasks
- POST /tasks
- PUT /tasks/{task_id}
- DELETE /tasks/{task_id}