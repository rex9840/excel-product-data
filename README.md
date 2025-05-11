# excel-product-data

To design and implement a Django-based feature that reads and validates an uploaded Excel file containing product data, processes the data efficiently, logs outcomes, and provides analytics through an API.

Tasks: [link](https://docs.google.com/document/d/1gWuUSzC8LrMMXT9I9QqyGcbJbCAiZDFV89m-Otcfg7U/edit?pli=1&tab=t.0)

Authors = [rex9840](https://github.com/rex9840)

webiste: [https://task.rupeshnepal.com.np](https://task.rupeshnepal.com.np/swagger/)

## Sequence Diagram 


![tasks import_export (1)](https://github.com/user-attachments/assets/8a8fa18d-c519-45df-b7d6-135b3cc39d10)



## Setup Instruction: 
### requires-python = ``>=3.11``

### dependencies
```
    "django (>=5![tasks import_export (1)](https://github.com/user-attachments/assets/460e291a-ef88-44d2-952a-539a77047b59)
.2,<6.0)",
    "django-import-export (>=4.3.7,<5.0.0)",
    "openpyxl (>=3.1.5,<4.0.0)",
    "djangorestframework (>=3.16.0,<4.0.0)",
    "django-filter (>=25.1,<26.0)",
    "python-dotenv (>=1.1.0,<2.0.0)",
    "celery[redis] (>=5.5.2,<6.0.0)",
    "drf-yasg (>=1.21.10,<2.0.0)",
    "django-celery-results (>=2.6.0,<3.0.0)",
    "pandas (>=2.2.3,<3.0.0)",
    "gunicorn (>=23.0.0,<24.0.0)",
    "django-cors-headers (>=4.7.0,<5.0.0)",
    "honcho (>=2.0.0,<3.0.0)",
    "flower (>=2.0.1,<3.0.0)",
    "psycopg2-binary (>=2.9.10,<3.0.0)",
```

### Manual Server Setup: 
Instruction Steps: 
  - For Django Server:

```sh
git clone <repo-url>
cd project-directory
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt --force-reinstall 
python manage.py migrate
python manage.py runserver
```
  - For Celery:
```
celery -A core.celery worker --loglevel=info -E -Q default

```

### Automatic Dockerized Setup: 

COMMAND = `` make docker-compose  ``

what it does is run docker compose in your local machine spanning ``postgress``,``celery``,``flower``, ``dockerized backed``

### API DOC

#### Visit 

- ``/swagger/`` for interactive Swagger UI.
- ``/redocs/`` for api documentation.


#### Product Endpoints
| Method | Endpoint                 | Description                    |
| ------ | ------------------------ | ------------------------------ |
| GET    | `/api/v1/excel-import-export/product/`       | List all product items         |
| POST   | `/api/v1/excel-import-export/product/`       | Create a new product           |
| GET    | `/api/v1/excel-import-export/product/export` | Export product data to Excel   |
| POST   | `/api/v1/excel-import-export/product/import` | Import product data from Excel |


####  Logs Endpoints
| Method | Endpoint                    | Description                   |
| ------ | --------------------------- | ----------------------------- |
| GET    | `/api/v1/excel-import-export/logs/`             | List all logs                 |
| GET    | `/api/v1/excel-import-export/logs/latest/stats` | View latest import statistics |


### DEFAULT 

#### SUPERUSER: 

- username: ``admin``
- password : ``admin``
- email  : ``admin@admin.com``





