migration:
	python manage.py makemigrations --no-input
	python manage.py migrate --no-input 
	python manage.py createsuperuseradmin

runserver:
	make migration
	python manage.py collectstatic --no-input 
	python manage.py runserver 0.0.0:8000 


docker-compose:
	docker compose -f docker-compose.local.yml up --build --remove-orphans 

