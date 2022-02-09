FROM python:3.9.7-slim
WORKDIR /app
COPY ./requirements.txt /app
RUN pip install -r requirements.txt
COPY . .
CMD gunicorn foodgram.wsgi:application --bind 0.0.0.0:8000