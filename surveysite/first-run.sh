#!/usr/bin/env bash

# run on first docker-compose up

  docker-compose run web python manage.py makemigrations 
  docker-compose run web python manage.py migrate
  docker-compose run web python manage.py createsuperuser


#  now navigate to http://localhost:8000/admin to create a survey

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  xdg-open http://localhost:8000/admin
  xdg-open http://localhost:8000/survey
elif [[ "$OSTYPE" == "darwin"* ]]; then
  open http://localhost:8000/admin
  open http://localhost:8000/survey
fi