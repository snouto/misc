__author__ = 'root'

import time

class SmithWaterman(object):

    firstSequence = None
    secondSequence = None
    scoringMatrix = None

    match = 1
    mismatch = -1
    gap = -2
    m = 0
    n = 0
    firstSeq = str("")
    secondSeq = str("")
    thirdSeq = str("")

    before = 0
    after = 0

    def __init__(self,first,second):
        self.firstSequence = first
        self.secondSequence = second
        self.m = len(first)
        self.n = len(second)
        self.scoringMatrix = [[0 for x in range(self.n+1)] for y in range(self.m+1)]



    def run(self):

        before = int(round(time.time() * 1000))
        print("before :%d" % before)
        self.scoring()
        self.align(self.m,self.n)

        after  = int(round(time.time()*1000))
        print("after : %d" % after)
        diff = after - before

        print("Operation took : %f seconds" % (int(diff) / 1000.0))

        print(self.firstSeq)
        print(self.thirdSeq)
        print(self.secondSeq)



    def scoring(self):
        self.firstPass()

        for i in range(1,self.m+1):
            for j in range(1,self.n+1):
                self.scoringMatrix[i][j] = self.getMax(
                    self.scoringMatrix[i-1][j] + self.gap,
                    self.scoringMatrix[i][j-1] + self.gap,
                    self.scoringMatrix[i-1][j-1] + self.isMatch(self.firstSequence[i-1] , self.secondSequence[j-1])
                )


    def align(self,i,j):

        if i <=0 and j <=0:
            return;

        if ((self.scoringMatrix[i-1][j] + self.gap == self.scoringMatrix[i][j])):
            self.align(i-1,j)
            self.firstSeq += self.firstSequence[i-1]
            self.thirdSeq +=" "
            self.secondSeq += '-'

        elif (((self.scoringMatrix[i-1][j-1]+self.isMatch(self.firstSequence[i-1],self.secondSequence[j-1]))
                   == self.scoringMatrix[i][j])):
            self.align(i-1,j-1)
            self.firstSeq += self.firstSequence[i-1]
            self.secondSeq += self.secondSequence[j-1]
            self.thirdSeq += "||"
        else:
            self.align(i,j-1)
            self.firstSeq+='-'
            self.secondSeq += self.secondSequence[j-1]
            self.thirdSeq +=" "




    def getMax(self,A,B,C):
        Z  = max(A,B)
        return max(Z,C)

    def isMatch(self,first,second):

        if(first == second):
            return self.match
        else:
            return self.mismatch


    def firstPass(self):

        for x in range(0,self.m):
            self.scoringMatrix[x][0] = x * self.gap

        for y in range(0,self.n):
            self.scoringMatrix[0][y] = y * self.gap








    def printMatrix(self):
        print(self.scoringMatrix)



