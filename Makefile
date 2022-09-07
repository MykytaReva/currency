SHELL := /bin/bash

run:
	python app/manage.py runserver

shell_plus:
	python app/manage.py shell_plus --print-sql

makemigrations:
	python app/manage.py makemigrations

migrate1:
	python app/manage.py migrate

celery beat:
	cd app && celery -A settings beat --loglevel=INFO

celery worker:
	cd app && celery -A settings worker --loglevel=INFO

migrate: makemigrations \
	migrate1



