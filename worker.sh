#!/usr/bin/env bash
# Hello World Program in Bash Shell

echo "Iniciando worker"
python manage.py celeryd -l info
echo "Iniciando python manage.py celery info"
celery -A gettingstarted beat --app=gettingstarted.celeryApp:app -l debug --max-interval=120
echo "Iniciando celery getting started"
