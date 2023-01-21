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
## Run the dind worker

```
docker run --privileged --name dind -d -p 2375:2375 \
    -e MYMATH_TAG=SOME_VERSION dind-practice:SOME_VERSION
```
## Build mymath images in dind

```
docker exec dind docker compose build
```

## Run the Celery woker server as a Docker container

```
docker run --name celery -d -p 5000:5000 -e REDIS_DOMAIN=10.32.124.136 \
    -e DIND_IP=10.32.124.136 -e MYMATH_TAG=1.0 \
    -e RUN_ENV=development celery-practice:1.0
```