#!/usr/bin/python
import random

__author__ = 'root'

import sys
import time

class StopWatch(object):
    start = 0
    now = 0
    def __init__(self):
        self.start = int(time.time())

    def elapsedTime(self):
         self.now  = int(time.time())
         return (self.now-self.start)




def algorithm(contents):
    cnt = 0
    count = len(contents)

    for i in range(0,count):
            for j in range(i+1,count):
                for k in range(j+1,count):
                    if contents[i] + contents[j] + contents[k] == 0:
                        cnt += 1


def main():
    args = sys.argv[1:]
    count = None
    stopwatch = None
    cnt = 0
    contents = []
    outputFile = args[1]

    try:



        count = int(args[0])

        print("Starting the analysis for the current algorithm")

        file = open(outputFile,mode='w')
        file.write("Count;Seconds\n")

        while count <= 500000:
            contents = [0  for x in range(count)]

            for x in range(count):
                contents[x] = random.randint(-sys.maxint,sys.maxint)

            stopwatch = StopWatch()
            algorithm(contents)
            stopwatch.elapsedTime()
            file.write('%s;%s\n' %(count,stopwatch.now-stopwatch.start))
            file.flush()
            count += count







    except Exception as exc:
        print(exc)
        return



if __name__ =='__main__':
    main()
