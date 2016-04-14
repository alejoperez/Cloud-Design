#!/usr/bin/env bash
# Hello World Program in Bash Shell

celery -A gettingstarted beat --app=gettingstarted.celeryApp:app -l debug --max-interval=120 & python manage.py celeryd -l info
