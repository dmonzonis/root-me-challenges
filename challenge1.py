from time import sleep
from math import sqrt

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
    response = send_private_message(irc_socket, "Candy", ":!ep1")
    x, y = [int(n) for n in response.split(':')[-1].split(' / ')]
    print("Got numbers: %s, %s" % (x, y))
    result = round(sqrt(x) * y, 2)
    print("Sending result")
    # Print final response
    print(send_private_message(irc_socket, "Candy", ":!ep1 -rep %f" % result))


if __name__ == "__main__":
    main()
