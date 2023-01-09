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
## Build Dockerfile

```
TAG=SOME_VERSION docker-compose build --no-cache
```

## Run the Celery woker server as a Docker container

```
docker run --name celery -d -e REDIS_DOMAIN=SOME_IP \
    -e RUN_ENV=development celery-practice:SOME_VERSION
```
