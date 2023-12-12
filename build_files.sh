#!/bin/bash
pip -m install -r requirements.txt
python3.9 manage.py collectstatic --noinput