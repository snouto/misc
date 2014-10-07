#!/usr/bin/python
from smithwaterman import SmithWaterman
import sys

__author__ = 'root'


import time


def main():

    sys.setrecursionlimit(sys.getrecursionlimit() * 4)

    firstFile = open("/home/snouto/Desktop/sequence.fasta","r")
    secondFile = open("/home/snouto/Desktop/second.fasta","r")
    firstSeq = firstFile.read()[0:3000]
    secondSeq =secondFile.read()[0:3000]
    smith = SmithWaterman(firstSeq,secondSeq)
    smith.run()



if __name__ == '__main__':
    main()



