from mymath.tasks import add

result = add.delay(4, 4)
try:
    result.get(timeout=1)
    print('Result for add(4, 4) is %d' % (result.get(timeout=1)))
except:
    print("Failed to run add(4, 4) task in celery.")