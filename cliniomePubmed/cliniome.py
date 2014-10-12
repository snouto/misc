#!/usr/bin/python3



__author__ = 'root'
import os
import urllib.request

"""

This file will read the urls from the Datasets file

"""


class Downloader(object):

    user = None
    Password = None
    directory = None
    counter = 0
    def __init__(self,user,passwd,directory):
        self.user = user
        self.Password = passwd
        self.directory = directory

    def downloadFile(self,url):
        try:

            p = urllib.request.HTTPPasswordMgrWithDefaultRealm()

            p.add_password(None, url, self.user, self.Password)

            handler = urllib.request.HTTPBasicAuthHandler(p)
            opener = urllib.request.build_opener(handler)
            urllib.request.install_opener(opener)

            fileToDownload = urllib.request.urlopen(url)
            fileName = url.split('/')[-1]
            fullPath = self.directory+"/" + fileName

            with open(fullPath,'wb') as downloaded_file:
                downloaded_file.write(fileToDownload.read())

            self.counter += 1

            print("Done downloading the current File (%d) Named : %s" % (self.counter,fileName))


        except Exception as exec:
            print("Exception : %s , URL : %s" %(exec,url))


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

                downloader = Downloader(user,passwd,currentDir)
                downloader.downloadFile(url)

            counter += 1


    except Exception as exec:
        print(exec)

def fileExists(dirWithFile):
    return os.path.exists(dirWithFile)








if __name__ =='__main__':
    main()

