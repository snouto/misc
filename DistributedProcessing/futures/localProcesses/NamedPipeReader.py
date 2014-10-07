"""

This python script shows the development of a Named Pipe Reader , which reads data from a Named Pipe
to read data delivered through another local process on the same machine .

Named Pipe differs from normal Pipe in that NamedPipe represents a physical file which has a file descriptor (the name
 of the named Pipe) that both writer and reader and write or read messages from respectively

"""

__author__ = 'snouto'

import os


namedPipe = "mynamedPipe"

def read_pipe(pipe):
    fd = os.open(pipe,os.O_RDONLY)
    #message = "Process [%d] Received a Message [%s]" % (os.getpid(),str(os.read(fd,22)))
    message = os.read(fd,1024)
    print(str(message))
    os.close(fd)

def main():

    read_pipe(namedPipe)




if __name__ =='__main__':
    main()
