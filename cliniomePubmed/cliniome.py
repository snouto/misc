#!/usr/bin/python3

from cliniomePubmed import Downloader

__author__ = 'root'
import os

"""

This file will read the urls from the Datasets file

"""

files = ['/home/snouto/bioinformatics/medlease.txt','/home/snouto/bioinformatics/medleasebaseline.txt']
directory = '/home/snouto/bioinformatics/files'
dirNames = ['medlease','medleasebaseline']
user = 'ibrahim'
passwd = 'riyadh'

def main():
    try:
        counter = 0

        for file in files:
            urls = open(file,'r').read().split()
            for url in urls:
                currentDir = directory +"/" + dirNames[counter]

                fileName = url.split('/')[-1]
                if not (fileName.split('.')[-1] == 'gz'):
                    continue

                if fileExists(currentDir+"/"+fileName):
                    continue

                downloader = Downloader.Downloader(user,passwd,currentDir)
                downloader.downloadFile(url)

            counter += 1


    except Exception as exec:
        print(exec)

def fileExists(dirWithFile):
    return os.path.exists(dirWithFile)








if __name__ =='__main__':
    main()

