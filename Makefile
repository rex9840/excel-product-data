migration:
	python manage.py makemigrations --no-input
	python manage.py migrate --no-input 

create_superuser:
	python manage.py createsuperuser --no-input --username admin --email admin@admin.com --password admin 

prod:	
	make migration
	python manage.py collectstatic --no-input 
	make create_superuser
	python -m gunicorn core.wsgi:application \
	--bind 0.0.0.0:8000 -w 3 --log-level info  \
	--access-logfile /var/log/gunicorn/access.log \
	--error-logfile /var/log/gunicorn/error.log 
