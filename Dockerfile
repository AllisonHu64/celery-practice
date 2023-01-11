ARG PYTHON_VERISON=3.8.9
FROM python:${PYTHON_VERISON}

WORKDIR /usr/ahu/code/
ENV FLASK_APP=entrypoint.py
ENV FLASK_RUN_HOST=0.0.0.0
# RUN git clone https://github.com/AllisonHu64/celery-practice.git
COPY ./ celery-practice/

WORKDIR /usr/ahu/code/celery-practice
RUN pip install -r requirements.txt
ENTRYPOINT ["sh", "./start.sh"]
EXPOSE 5000