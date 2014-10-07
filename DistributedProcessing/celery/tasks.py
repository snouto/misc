__author__ = 'root'


"""

To run this file
================
Place it in a directory on your machine , open linux shell on that directory (Assuming that you have already installed Celery

to install Celery
=================
pip install celery

to install Redis (As our broker to distribute tasks among workers)
==================================================================

pip install celery[redis]

then on command prompt on the directory that contains this file  , write the following


$ celery -A tasks worker --loglevel=info




"""

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
