import os 
from celery import Celery,Task

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings') 

app = Celery("excel_import_export")
app.config_from_object("django.conf:settings", namespace="CELERY") 
app.autodiscover_tasks() 
app.conf.update()



# celery -A core.celery worker --loglevel=info -E -Q default
class BaseTaskWithRetry(Task):
    retry_kwargs = {"max_retries": 5}
    max_retries = 5
    retry_backoff = True
    retry_backoff_max = 60 * 5  # 5 minutes
    retry_jitter = True
    options = {"queue": "default"}
    time_limit = 60 * 5  # 5 minutes
    queue = "default"
    rate_limit = "6/s"

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        super().on_failure(exc, task_id, args, kwargs, einfo)
        self.retry(exc=exc, countdown=60 * 5)

