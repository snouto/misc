"""

This python script represents a way to execute parallel tasks using Multiple Threads on a single machine
utilizing the ThreadPoolExecutor Class that acts as a Thread Pool to manage and recycle already initialized
Threads , It takes care about the synchronization between threads

"""


__author__ = 'snouto'
import sys
import concurrent.futures
import time
import threading
from threading import Thread

from concurrent.futures.thread import ThreadPoolExecutor

def fibonacci(number):
    a,b=0,1

    for item in range(number):
        a,b = b,a+b
        print ("current Thread name : %s" % threading.current_thread().name)
    return a


def main():

    with ThreadPoolExecutor(max_workers=5) as executor:
        for item in range(20):
            future  = executor.submit(fibonacci,item)

            print ("current result : %d" % future.result())


if __name__ == '__main__':
    main()
