from __future__ import absolute_import
import os
import django
from celery import Celery
from django.conf import settings
from django.core.wsgi import get_wsgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'gettingstarted.settings'
application = get_wsgi_application()
#django.setup()

app = Celery('tasks')

app.config_from_object('django.conf:settings')
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)