up:
	docker-compose up -d --build

down:
	docker-compose down

logs:
	docker-compose logs -f backend

migrations:
	docker-compose exec backend python manage.py makemigrations

migrate:
	docker-compose exec backend python manage.py migrate

test:
	docker-compose exec backend python manage.py test

superuser:
	docker-compose exec backend python manage.py createsuperuser