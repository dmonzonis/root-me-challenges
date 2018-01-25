from time import sleep

from irc import connect_to_host, join_channel, send_private_message


# Globals
HOST = "irc.root-me.org"
PORT = 6667
CHANNEL = "#root-me_challenge"
NICK = "rumplerino"


def get_challenge_input(challenge_number, host=HOST, port=PORT, nick=NICK):
    """Connect to the IRC and join channel, and return the socket and the challenge input."""
    # Connect to the IRC and join room
    irc_socket = connect_to_host(host, port, nick)
    # Give some time to authenticate before joining channel
    sleep(2)
    join_channel(irc_socket, CHANNEL)

    response = send_private_message(irc_socket, "Candy", ":!ep%s" % str(challenge_number))
    return irc_socket, response


def send_solution(irc_socket, challenge_number, solution, host=HOST, port=PORT, nick=NICK):
    """Send solution through the IRC socket, and return feedback."""
    feedback = send_private_message(irc_socket, "Candy", ":!ep%s -rep %s" % (
        str(challenge_number), solution
    ))
    return feedback
