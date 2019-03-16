import os
from celery import Celery
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'Scraping.settings')

app = Celery('Scraping')
app.config_from_object('django.conf:settings')
# app.autodiscover_tasks()



app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)