#!/usr/bin/python3

__author__ = 'root'

"""
This file is used to download files from the NCBI Pubmed and Medlease Databases

"""

import urllib.request

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
            fullPath = self.directory + fileName

            with open(fullPath,'wb') as downloaded_file:
                downloaded_file.write(fileToDownload.read())

            self.counter += 1

            print("Done downloading the current File (%d) Named : %s" % (self.counter,fileName))


        except Exception as exec:
            print("Exception : %s , URL : %s" %(exec,url))
