__author__ = 'root'

from math import sqrt
from celery import Celery

import time

app = Celery('tasks',broker='redis://localhost:6379/0')

app.conf.CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'

app.conf.counter = 2


@app.task
def squareroot(value):
    return sqrt(value)

@app.task
def calc_fib(value):
    d = time.time()
    a ,b = 0 , 1
    time.sleep(app.conf.counter)
    app.conf.counter+=2

    for x in range(value):
        a , b = b , a+b

    after = int(round(time.time()*1000))

    return (value,"Started at %d , Took :%d by process ID : {%s} and result : %d" %(int(round(d * 1000)),
                                                                                    (after-int(round(d*1000)))
                                                                                    ,calc_fib.request.id,a))
