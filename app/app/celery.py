import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'app.settings')

app = Celery('app')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.conf.enable_utc = False

app.conf.update(timezone = 'Asia/Kolkata')


# Celery Beat Settings
app.conf.beat_schedule = {
    'price-feeds-from-alphavantage': {
        'task': 'core.tasks.get_price_feed',
        'schedule': 3600.0,
        #'args': (2,)
    }
    
}

app.autodiscover_tasks()

@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')