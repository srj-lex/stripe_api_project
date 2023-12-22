#!/bin/bash
cd stripe_api_project
python3 manage.py migrate
python3 manage.py load_items
python3 manage.py runserver 0:8000