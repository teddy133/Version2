FROM python:2

ENV PYTHONUNBUFFERED 1
RUN apt-get update
RUN mkdir /code
WORKDIR /code
COPY . /code/
RUN pip install -r requirements.txt
EXPOSE 8000
RUN python manage.py makemigrations gamers
RUN python manage.py migrate
