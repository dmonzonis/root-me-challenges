import socket
import string
import time
from math import sqrt

#Settings
HOST = "irc.root-me.org"
PORT = 6667
CHANNEL = "#root-me_challenge"
NICK = "rumplerino"

#Open socket
def openSocket():
    ircSocket = socket.socket()
    ircSocket.connect((HOST, PORT))
    ircSocket.send("NICK " + NICK + "\r\n")
    ircSocket.send("USER guest host bla :Cadamino\r\n")
    #Give some time to authenticate before joining channel
    time.sleep(3)
    ircSocket.send("JOIN " + CHANNEL + "\r\n")
    return ircSocket

#Wait until connected to the channel and display message
def joinRoom(sock):
    readBuffer = ""
    Loading = True
    while Loading:
        readBuffer = readBuffer + sock.recv(1024)
        temp = string.split(readBuffer, "\n")
        readBuffer = temp.pop()
        for line in temp:
            print(line)
            if "End of /NAMES list" in line:
                Loading = False
    print "Connected!"

#Send message, interpret result and respond with solution
def sendMessage(sock):
    readbuffer = ""
    sock.send("PRIVMSG candy :!ep1\r\n")
    while True:
        readbuffer = readbuffer + sock.recv(1024)
        temp = string.split(readbuffer, "\n")
        readbuffer = temp.pop()
        print temp
        for line in temp:
            if "Candy" in line:
                #Message comes from candy
                response = line
                num = response.split(':')[2].split('/')
                result = sqrt(int(num[0])) * int(num[1])
                print "Sending result %f..."%result
                sock.send("PRIVMSG candy :!ep1 -rep %.2f\r\n"%round(result,2))
                #Check for a response
                readbuffer = readbuffer + sock.recv(1024)
                temp = string.split(readbuffer, "\n")
                readbuffer = temp.pop()
                for r in temp:
                    print r
                break

ircSocket = openSocket()
joinRoom(ircSocket)
sendMessage(ircSocket)
