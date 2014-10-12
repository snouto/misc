__author__ = 'root'

import urllib


#https://ftp.nlm.nih.gov/projects/medlease/gz/medline14n0747.xml.gz

import urllib.request
# Create an OpenerDirector with support for Basic HTTP Authentication...
#auth_handler = urllib.request.HTTPBasicAuthHandler()
"""
auth_handler.add_password(realm='ftp.nlm.nih.gov',
                          uri='http://ftp.nlm.nih.gov/projects/medlease/gz/medline14n0747.xml.gz',
                          user='ibrahim',
                          passwd='riyadh')
"""

#opener = urllib.request.build_opener(auth_handler)
# ...and install it globally so it can be used with urlopen.
#urllib.request.install_opener(opener)
url = 'http://ftp.nlm.nih.gov/projects/medlease/gz/medline14n0747.xml.gz'
username = 'ibrahim'
password = 'riyadh'
p = urllib.request.HTTPPasswordMgrWithDefaultRealm()

p.add_password(None, url, username, password)

handler = urllib.request.HTTPBasicAuthHandler(p)
opener = urllib.request.build_opener(handler)
urllib.request.install_opener(opener)

fileToDownload = urllib.request.urlopen('http://ftp.nlm.nih.gov/projects/medlease/gz/medline14n0747.xml.gz')

with open('/home/snouto/Desktop/medline14n0747_2.xml.gz','wb') as downloaded_file:
    downloaded_file.write(fileToDownload.read())


print("Done downloading the current File")