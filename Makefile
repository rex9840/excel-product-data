migration:
	python manage.py makemigrations --no-input
	python manage.py migrate --no-input 

prod:	
	make migration
	python manage.py collectstatic --no-input 
	python -m gunicorn core.wsgi:application \
	--bind 0.0.0.0:8000 -w 3 --log-level info  \
	--access-logfile /var/log/gunicorn/access.log \
	--error-logfile /var/log/gunicorn/error.log 
