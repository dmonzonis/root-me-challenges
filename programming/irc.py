import socket


def connect_to_host(host, port, nick='guest'):
    """Connect to an IRC channel and return the socket with the connection."""
    ircSocket = socket.socket()
    ircSocket.connect((host, port))
    ircSocket.send(("NICK " + nick + "\r\n").encode('utf-8'))
    ircSocket.send("USER guest host asdf :Cadamino\r\n".encode('utf-8'))
    print("Connected")
    return ircSocket


def join_channel(sock, channel):
    """Join a channel and wait until the connection is completed."""
    # Join channel
    sock.send(("JOIN " + channel + "\r\n").encode('utf-8'))
    # Wait until successfully connected
    response = ""
    while response.find("End of /NAMES list.") == -1:
        response = sock.recv(2048).decode('utf-8')
        response = response.strip('\r\n')
    print("Room joined")


def send_private_message(sock, user, msg):
    """Send a private message to the specified user and return the response.

    Already includes the carriage return and newline, so there's no need to send it within the
    message.
    """
    msg = msg.strip('\r\n')  # Strip carriage return and newline if it was put by the caller
    sock.send(("PRIVMSG %s %s\r\n" % (user, msg)).encode('utf-8'))
    response = sock.recv(2048).decode('utf-8').strip('\r\n')
    return response
