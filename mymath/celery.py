from celery import Celery
import os

run_env = os.environ.get('RUN_ENV') or 'local'
if run_env == 'local':
    app = Celery('mymath', backend='redis://localhost', broker='redis://localhost', 
                include=['mymath.tasks'])
elif run_env == 'development':
    redis_domain = os.environ.get('REDIS_DOMAIN')
    redis_url = 'redis://{}'.format(redis_domain)
    app = Celery('mymath', backend=redis_url, broker=redis_url, include=['mymath.tasks'])

if __name__ == '__main__':
    app.start()