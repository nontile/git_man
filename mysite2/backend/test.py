from celery import Celery

app = Celery('test', broker='amqp://sktl:sktl01@192.168.200.118:5672/sktl')
# app = Celery('test', broker='amqp://alis:alis1234!@#$@192.168.200.118:5672/myvhost')


@app.task
def add(x, y):
    return x + y


task.de