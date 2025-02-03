import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'seu_projeto.settings')

app = Celery('seu_projeto')
app.config_from_object('django.conf:settings', namespace='CELERY')
app.autodiscover_tasks()