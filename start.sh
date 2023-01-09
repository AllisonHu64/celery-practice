celery -A mymath multi start worker1 --loglevel=INFO \
    --logfile="./log/celery/worker1.log" \
    --pidfile="./run/celery/worker1.pid"
flask run