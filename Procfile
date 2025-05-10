web: python -m gunicorn core.wsgi:application --bind 0.0.0.0:8000 -w 1  --log-level info --access-logfile /var/log/gunicorn/access.log --error-logfile /var/log/gunicorn/error.log
worker: celery -A core.celery  worker --loglevel=info --concurrency=1  -Q default 

