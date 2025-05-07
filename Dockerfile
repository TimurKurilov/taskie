FROM python:3.11-slim

RUN mkdir /app

RUN apt update && apt install vim -y

COPY requirements.txt /app
RUN pip install -r /app/requirements.txt --no-cache-dir

COPY taskie/ /app

WORKDIR /app

CMD ["gunicorn", "taskie.wsgi:application", "--bind", "0:8000" ]