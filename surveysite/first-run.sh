#!/usr/bin/env bash

# run on first docker-compose up

docker-compose run web python manage.py makemigrations 
docker-compose run web python manage.py migrate
# DJANGO_SUPERUSER_PASSWORD="Foobar1234" docker-compose run web python manage.py createsuperuser --username root --email root@example.com
echo "from django.contrib.auth.models import User; User.objects.create_superuser('root', 'root@example.com', 'password')" | docker-compose run web python manage.py shell

docker-compose run -e PYTHONPATH='/code'  -e DJANGO_SETTINGS_MODULE='surveysite.container' web django-admin loaddata data-dump.json


#  now navigate to http://localhost:8000/admin to create a survey

if [[ "$OSTYPE" == "linux-gnu"* ]]; then
  #  xdg-open http://localhost:8000/admin
  xdg-open http://localhost:8000/survey
elif [[ "$OSTYPE" == "darwin"* ]]; then
  #  open http://localhost:8000/admin
  open http://localhost:8000/survey
fi