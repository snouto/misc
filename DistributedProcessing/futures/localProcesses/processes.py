"""
This python script shows how we can create two different local processes on the local machine to coordinate tasks
between them , it uses Pipe as the communication channel to deliver tasks between different coordinating processes
on the local machine
"""

__author__ = 'snouto'

import os , random , time
from multiprocessing import Process , Pipe
from threading import Thread

def producer_task(conn):

        for item in range(20):
            number = random.randint(item,100)
            conn.send(number)

    #print ("Sending Value %d from Process : %d" % (number , os.getpid()))
        conn.close() #closing the Pipe Channel


def consumer_task(conn):
        receivedNumber = conn.recv()
        print ("Consumer Process ID : %d and received Number is : %d" %(os.getpid(),receivedNumber))



if __name__ =='__main__':

    producer_conn , consumer_conn = Pipe()

    producer = Process(target=producer_task,args=(producer_conn,))
    consumer = Process(target=consumer_task,args=(consumer_conn,))

    #start each of the producer and consumer tasks
    producer.start()
    consumer.start()

    #then let them join
    producer.join()
    consumer.join()


