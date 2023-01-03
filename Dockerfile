ARG PYTHON_VERISON=3.8.9
FROM python:${PYTHON_VERISON}

WORKDIR /usr/ahu/code/
RUN git clone https://github.com/AllisonHu64/celery-practice.git

WORKDIR /usr/ahu/code/celery-practice
RUN pip install -r requirements.txt
ENTRYPOINT ["celery", "-A", "tasks", "worker", "--loglevel=INFO"]