import zlib
import base64

from challenge_utils import get_challenge_input, send_solution


def main():
    """Solve challenge 4: Uncompress me."""
    sock, response = get_challenge_input(4)
    encoded = response.split(':')[-1]
    print("Got encoded string: %s" % encoded)
    solution = zlib.decompress(base64.b64decode(encoded)).decode('utf-8')
    print("Sending solution")
    print(send_solution(sock, 4, solution))


if __name__ == "__main__":
    main()
