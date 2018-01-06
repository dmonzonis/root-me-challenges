import requests
import re


URL = 'http://challenge01.root-me.org/programmation/ch1/'


def sequence(a, b, n, start):
    """Compute the value n of a sequence of the form U_{n+1} = a + U_{n} + n * b; U_{0} = c."""
    result = start
    for count in range(n):
        result = a + result + count * b
    return result


def get_parameters(html):
    """Get parameters from the challenge page.

    The sequence is of the form U_{n+1} = a + U_{n} + n * b; U_{0} = c.
    The challenge page also specifies the order up to which to compute the sequence, n.
    This method returns a tuple containing (a, b, c, n).
    """
    numbers = [int(x) for x in re.findall('-?\d+', html)]
    signs = [s for s in re.findall('[+-]', html)]
    # If there's a minus sign, absorb it into the b parameter
    if signs[3] == '-':
        numbers[2] *= -1
    return numbers[1], numbers[2], numbers[4], numbers[5]


def main():
    """Solve challenge 6: Arithmetic progression."""
    # Load session and grab parameters
    session = requests.Session()
    page = session.get(URL)
    a, b, start, n = get_parameters(page.text)
    print("Got parameters. Computing solution...")

    # Compute solution and send it for validation
    solution = sequence(a, b, n, start)
    print("Solution found: " + str(solution))
    print("Sending solution and printing response page")
    resp = session.get(URL + 'ep1_v.php?result=' + str(solution))
    print(resp.text)


if __name__ == "__main__":
    main()
