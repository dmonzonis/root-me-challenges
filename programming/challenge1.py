from math import sqrt

from challenge_utils import get_challenge_input, send_solution


def main():
    """Solve challenge 1: Go back to college."""
    sock, response = get_challenge_input(1)
    x, y = [int(n) for n in response.split(':')[-1].split(' / ')]
    print("Got numbers: %s, %s" % (x, y))
    solution = round(sqrt(x) * y, 2)
    print("Sending solution")
    print(send_solution(sock, 1, solution))


if __name__ == "__main__":
    main()
