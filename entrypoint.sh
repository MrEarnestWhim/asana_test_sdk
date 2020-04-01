#!/bin/bash

set -e
./manage.py migrate
./manage.py createadmin
./manage.py runserver 0.0.0.0:8000