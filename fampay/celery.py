import os
from celery import Celery
from celery.schedules import crontab

os.environ.setdefault('FORKED_BY_MULTIPROCESSING', '1')
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'fampay.settings')

app = Celery('fampay')

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()

app.conf.beat_schedule = {
    'fetch_youtube_videos': {
        'task': 'youtube.tasks.fetch_videos',
        'schedule': crontab(minute=1),
    },

    'sample_task': {
        'task': 'youtube.tasks.sample_task',
        'schedule': 5.0,
    }
}
