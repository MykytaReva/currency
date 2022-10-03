SHELL := /bin/bash

run:
	python app/manage.py runserver

shell_plus:
	python app/manage.py shell_plus --print-sql

show_urls:
	python app/manage.py show_urls

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

pytest:
	pytest app/tests/

coverage:
	pytest --cov=app app/tests/ --cov-report html && coverage report --fail-under=79.0000

show-coverage:  ## open coverage HTML report in default browser
	python3 -c "import webbrowser; webbrowser.open('.pytest_cache/coverage/index.html')"