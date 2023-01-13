ARG PYTHON_VERISON=3.8.9
FROM python:${PYTHON_VERISON}

WORKDIR /usr/ahu/code/
COPY div.py div.py
ENTRYPOINT ["python", "div.py"]