from mymath.tasks import add, sub, mul, div
from flask import Flask
import os

flask_app = Flask(__name__)

@flask_app.route("/add/<int:num1>/<int:num2>")
def myadd(num1, num2):
    result = add.delay(num1, num2)
    try:
        return 'Result for add(%d, %d) is %d.\n' % (num1, num2, result.get(timeout=1))
    except Exception as e:
        return 'Failed to run add(%d, %d) task in celery.\n' % (num1, num2)

@flask_app.route("/sub/<int:num1>/<int:num2>")
def mysub(num1, num2):
    result = sub.delay(num1, num2)
    try:
        return 'Result for sub(%d, %d) is %d.\n' % (num1, num2, result.get(timeout=1))
    except Exception as e:
        return 'Failed to run sub(%d, %d) task in celery.\n' % (num1, num2)

@flask_app.route("/mul/<int:num1>/<int:num2>")
def mymul(num1, num2):
    result = mul.delay(num1, num2)
    try:
        return 'Result for mul(%d, %d) is %d.\n' % (num1, num2, result.get(timeout=1))
    except Exception as e:
        return 'Failed to run mul(%d, %d) task in celery.\n' % (num1, num2)

@flask_app.route("/div/<int:num1>/<int:num2>")
def mydiv(num1, num2):
    result = div.delay(num1, num2)
    try:
        return 'Result for div(%d, %d) is %d.\n' % (num1, num2, result.get(timeout=1))
    except Exception as e:
        return 'Failed to run div(%d, %d) task in celery.\n' % (num1, num2)