DJANGO_MANAGE=python manage.py
SUPERUSER_USERNAME=admin
SUPERUSER_EMAIL=admin@admin.com
SUPERUSER_PASSWORD=admin

migration:
	python manage.py makemigrations --no-input
	python manage.py migrate --no-input 

createsuperuser:
	@if ! $(DJANGO_MANAGE) shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(username='$(SUPERUSER_USERNAME)').exists())"; then \
		echo "Creating superuser..."; \
		$(DJANGO_MANAGE) createsuperuser --no-input --username $(SUPERUSER_USERNAME) --email $(SUPERUSER_EMAIL) --password $(SUPERUSER_PASSWORD); \
	else \
		echo "Superuser already exists."; \
	fi

prod:	
	make migration
	python manage.py collectstatic --no-input 
	make createsuperuser
	python -m gunicorn core.wsgi:application \
	--bind 0.0.0.0:8000 -w 3 --log-level info  \
	--access-logfile /var/log/gunicorn/access.log \
	--error-logfile /var/log/gunicorn/error.log 
