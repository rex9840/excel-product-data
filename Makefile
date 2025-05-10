migration:
	python manage.py makemigrations --no-input
	python manage.py migrate --no-input 
	python manage.py createsuperuseradmin

run:
	make migration
	python manage.py collectstatic --no-input 
	honcho start

