from challenge_utils import get_challenge_input, send_solution


def rot13(s):
    from codecs import encode
    return encode(s, 'rot_13')


def main():
    """Solve challenge 3: The Roman's wheel."""
    sock, response = get_challenge_input(3)
    encoded = response.split(':')[-1]
    print("Got encoded string: %s" % encoded)
    solution = rot13(encoded)
    print("Sending solution")
    print(send_solution(sock, 3, solution))



if __name__ == "__main__":
    main()
