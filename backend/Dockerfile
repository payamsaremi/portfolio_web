FROM python:3.8.8-slim-buster

COPY requirements.txt /app/requirements.txt

RUN apt-get update && apt-get -y upgrade
RUN apt-get -y install build-essential && apt-get -y install libjpeg-dev
RUN apt-get -y install libmagic1
RUN pip install --upgrade pip
RUN pip install --default-timeout=100 --no-cache-dir -r /app/requirements.txt

WORKDIR /app

ADD . .

# EXPOSE 8000

# CMD ["gunicorn", "--bind", ":8000", "--workers", "3", "backend.wsgi:application"]

CMD gunicorn backend.wsgi:application --bind 0.0.0.0:$PORT