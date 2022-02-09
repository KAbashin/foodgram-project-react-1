#FROM python:3.7
#WORKDIR /app
#COPY . /app
#RUN pip3 install -r requirements.txt
#CMD ["gunicorn", "foodgram.wsgi:application", "--
FROM python:3.7
WORKDIR /code
COPY requirements.txt requirements.txt
RUN pip install --upgrade pip && pip install -r /code/requirements.txt
COPY . /code
CMD gunicorn foodgram_api.wsgi:application --bind 0.0.0.0:8000