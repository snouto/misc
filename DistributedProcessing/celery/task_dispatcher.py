#!/usr/bin/python
__author__ = 'root'

from celery import Celery

app = Celery('tasks',broker='redis://localhost:6379/0')
app.conf.CELERY_RESULT_BACKEND='redis://localhost:6379/0'


def call_sqrt(value):
    result = app.send_task('tasks.squareroot',args=(value,))
    print(result.get())

def call_fib(value_list):
    results = {x:app.send_task('tasks.calc_fib',args=(x,)) for x in value_list}

    for key , value in results.items():

        print("key : %d , value : %s" %(key,value.get()))



def main():


    for x in app.tasks:
        print(x)

    call_fib([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,1000])





if __name__ =='__main__':
    main()
