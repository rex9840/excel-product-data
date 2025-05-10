migration:
	python manage.py makemigrations --no-input
	python manage.py migrate --no-input 
	python manage.py createsuperuseradmin

run:
	make migration
	python manage.py collectstatic --no-input 
	honcho start

server:
	cp .env.example docker.env
	docker compose up --build 
