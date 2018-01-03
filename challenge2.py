import base64
from time import sleep

from irc import connect_to_host, join_channel, send_private_message


# Globals
HOST = "irc.root-me.org"
PORT = 6667
CHANNEL = "#root-me_challenge"
NICK = "rumplerino"


def main():
    """Solve the challenge, printing the output to console."""
    # Connect to the IRC and join room
    irc_socket = connect_to_host(HOST, PORT, NICK)
    # Give some time to authenticate before joining channel
    sleep(2)
    join_channel(irc_socket, CHANNEL)

    # Solve puzzle
    response = send_private_message(irc_socket, "Candy", ":!ep2")
    encoded = response.split(':')[-1]
    print("Got encoded string: %s" % encoded)
    result = base64.b64decode(encoded).decode('utf-8')
    print("Sending result")
    print(send_private_message(irc_socket, "Candy", ":!ep2 -rep %s" % result))


if __name__ == "__main__":
    main()
