MANAGE := python3 backend/manage.py
PYTHON := python3


venv:
	python3 -m venv venv

install:
	pip install -r backend/requirements.txt

db:
	docker-compose up -d

run:
	$(MANAGE) runserver

migrations:
	$(MANAGE) makemigrations

migrate:
	$(MANAGE) migrate

superuser:
	$(MANAGE) createsuperuser

freeze:
	pip freeze > backend/requirements.txt

stop:
	docker-compose down