SHELL := /bin/bash

build:
	cp -n .env.example .env && docker-compose up -d --build

run:
	uvicorn main:app --reload --host=0.0.0.0 --port=8000

logs_backend:
	docker logs -f backend

makemigrations:
	docker exec -it backend alembic revision --autogenerate -m "Added required tables"

migrate:
	docker exec -it backend alembic upgrade head