FROM python:3.11.0-slim AS builder
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update \
    && apt-get upgrade -y --no-install-recommends \
    && apt-get install -y git \ 
    && apt-get install -y make \ 
    && python3 -m  pip install --no-cache-dir --upgrade pip \
    && rm -rf /var/lib/apt/lists/*


COPY requirements.txt requirements.txt 
RUN pip install --no-deps --no-cache-dir -r requirements.txt 
COPY . . 
COPY .env.example docker.env
RUN chmod +x /app/start.sh
RUN  mkdir /var/log/gunicorn
RUN chmod  u+w /var/log/gunicorn
EXPOSE 8000 
CMD ["sh","/app/start.sh"]




