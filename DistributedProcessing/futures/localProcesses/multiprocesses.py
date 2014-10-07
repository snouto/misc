"""

This python script shows how we can utilize Pipe as channels for communicating different processes running on local machine
to coordinate tasks execution between them in parallel fashion, it utilizes Pipe as the main communication channel
to establish communication between different processes , it also creates consumer processes according to the number
of processor cores on the local machine

"""

__author__ = 'snouto'

import os , sys , random
from multiprocessing import Pipe,Process,cpu_count,current_process , Queue

q = Queue()
fibdict = {}
consumers = []

def producer_task(q,fibdict):
    for i in range(200):
        value  = random.randint(1,20)
        fibdict[value] = None
        q.put(value)


def fibonacci(number):
    a,b=0,1

    for item in range(number):
        a,b = b,a+b
    return a


def consumer_task(q,fibdict):

    while not q.empty():
        value = q.get(True,0.05)
        print ("Process : %d , Calculating value : %d" %(os.getpid(),value))
        result = fibonacci(value)
        fibdict[value] = result


if __name__ == '__main__':

    #create the producer
    producer = Process(target=producer_task,args=(q,fibdict,))
    producer.start()
    producer.join()
    #create the consumers to be the number of the count of available CPUs
    for cpu in range(cpu_count()):
        consumer = Process(target=consumer_task,args=(q,fibdict,))
        consumer.start()
        consumers.append(consumer)


    [consumer.join() for consumer in consumers]





