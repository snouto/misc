"""

This python script shows the development of a Named Pipe Writer , which Writes data to a Named Pipe that exists
 on the local machine

Named Pipe differs from normal Pipe in that NamedPipe represents a physical file which has a file descriptor (the name
 of the named Pipe) that both writer and reader and write or read messages from respectively

"""

__author__ = 'snouto'

import os


namedPipe = "mynamedPipe"


def write_to_pipe():

    if not os.path.exists(namedPipe):
        os.mkfifo(namedPipe)
    else:
        pass

    #write to the named pipe
    message = "Hello World from Process [%d]" %(os.getpid())
    writeMessage(namedPipe,message)


def writeMessage(pipe,message):

    fd = os.open(pipe,os.O_WRONLY)
    os.write(fd,bytes(message,'UTF-8'))
    os.close(fd)

def main():

    write_to_pipe()


if __name__ =='__main__':
    main()
