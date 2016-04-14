web: gunicorn gettingstarted.wsgi --log-file -
worker: celery -A gettingstarted beat --app=gettingstarted.celeryApp:app -l debug --max-interval=120
