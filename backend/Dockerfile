FROM python:3.7
RUN mkdir /app
WORKDIR /app
COPY ./requirements.txt .
RUN pip3 install -r ./requirements.txt --no-cache-dir
CMD ["gunicorn", "foodgram.wsgi:application", "--bind", "0:8000" ]