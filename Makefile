SHELL := /bin/bash

manage_py := docker exec -it backend python app/manage.py
run:
	$(manage_py) runserver

build:
	cp -n .env.example .env && docker-compose up -d --build

shell_plus:
	$(manage_py) shell_plus --print-sql

show_urls:
	$(manage_py) show_urls

makemigrations:
	$(manage_py) makemigrations

migrate1:
	$(manage_py) migrate

celery_beat:
	cd app && celery -A settings beat --loglevel=INFO

celery_worker:
	cd app && celery -A settings worker --loglevel=INFO

migrate: makemigrations \
	migrate1

pytest:
	docker exec -it backend pytest app/tests/

coverage:
	docker exec -it backend pytest --cov=app app/tests/ --cov-report html && coverage report --fail-under=79.0000

show-coverage:  ## open coverage HTML report in default browser
	python3 -c "import webbrowser; webbrowser.open('.pytest_cache/coverage/index.html')"

uwsgi_1:
	cd app && uwsgi --http-socket :8001 --module settings.wsgi --master --processes 17 --threads 4

uwsgi_2:
	cd app && uwsgi --http-socket :8002 --module settings.wsgi --master --processes 17 --threads 4 --stats 127.0.0.1:9192

good_uwsgi_1:
	cd app && uwsgi --ini uwsgi_1.ini

good_uwsgi_2:
	cd app && uwsgi --ini uwsgi_2.ini


rest_nginx:
	sudo /etc/init.d/nginx restart