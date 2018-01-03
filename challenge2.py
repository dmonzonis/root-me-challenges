import base64

from challenge_utils import get_challenge_input, send_solution


def main():
    """Solve challenge 2: Encoded string."""
    sock, response = get_challenge_input(2)
    encoded = response.split(':')[-1]
    print("Got encoded string: %s" % encoded)
    solution = base64.b64decode(encoded).decode('utf-8')
    print("Sending solution")
    print(send_solution(sock, 2, solution))


if __name__ == "__main__":
    main()
