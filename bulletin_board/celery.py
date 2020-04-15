import os

from celery import Celery
from django.conf import settings

# Set the default Django settings module
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "bulletin_board.config")
os.environ.setdefault("DJANGO_CONFIGURATION", "Local")

app = Celery("bulletin_board")

# Using a string here means the worker don't have to serialize the configuration object to child processes.
app.config_from_object("django.conf:settings")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
