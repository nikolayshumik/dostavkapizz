import os
from celery import Celery

# Установите переменную окружения с именем вашего проекта Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'dominopizza.settings')

app = Celery('dominopizza')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()