from celery import Celery
import os

run_env = os.environ.get('RUN_ENV') or 'local'
if run_env == 'local':
    app = Celery('tasks', backend='redis://localhost', broker='redis://localhost')
elif run_env == 'development':
    redis_domain = os.environ.get('REDIS_DOMAIN')
    redis_url = 'redis://{}'.format(redis_domain)
    app = Celery('tasks', backend=redis_url, broker=redis_url)

@app.task
def add(x, y):
    return x + y