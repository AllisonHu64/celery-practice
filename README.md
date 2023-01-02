# How to use

## Start a Redis Broker
Start a `Redis` instance with docker on port `6376`.
```
docker run --name my-redis -d -p 6379:6379 redis 
```

Run `redis-cli` to check that the `Redis` instance is successfully created.
```
$redis-cli 
redis 127.0.0.1:6379> 
redis 127.0.0.1:6379> PING  
PONG
```

## Install dependencies

Prepare venv under work directory
```bash
python3 -m venv venv
```

Activate the interpretor in project
```bash 
source venv/bin/activate
```

Install dependencies from pypi
```bash 
pip install -r requirements.txt
```

## Run the Celery woker server

```
celery -A tasks worker --loglevel=INFO
```

## Calling the tasks
```
python entrypoint.py
```

