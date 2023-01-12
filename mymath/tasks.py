from .celery import app
from handler.docker.docker_client_handler import DockerClientHandler

client = DockerClientHandler()

@app.task
def add(x, y):
    return client.run_mymath_add(x, y)

@app.task
def sub(x, y):
    return client.run_mymath_sub(x, y)

@app.task
def mul(x, y):
    return client.run_mymath_mul(x, y)

@app.task
def div(x, y):
    return client.run_mymath_div(x, y)
