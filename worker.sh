# Hello World Program in Bash Shell

echo "Iniciando worker"
celery -A gettingstarted beat --app=gettingstarted.celeryApp:app -l debug --max-interval=120
echo "Iniciando celery getting started"
python manage.py celeryd -l info
echo "Iniciando python manage.py celery info"
