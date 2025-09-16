FROM python:3.12.3-alpine3.18

LABEL authors="vidernykov.a.e@gmail.com"
ENV PYTHONUNBUFFERED 1

WORKDIR app/

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["celery", "-A", "tasks", "worker", "--loglevel=INFO"]
