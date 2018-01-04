import base64
from io import BytesIO
import re
import requests
from time import sleep

from bs4 import BeautifulSoup
from PIL import Image
import pytesseract


URL = 'http://challenge01.root-me.org/programmation/ch8/'


def get_image_string(html):
    """Get the captcha image on the given html string as a base64 string."""
    soup = BeautifulSoup(html, 'html5lib')
    img_string = soup.img['src'].split(',')[-1]
    return img_string


def base64_to_image(s):
    """Convert base64 string to image and return the Image object."""
    return Image.open(BytesIO(base64.b64decode(s)))


def remove_black(img):
    """Change all black pixels to white on an image."""
    pixels = img.load()  # Load pixel map
    w, h = img.size  # Get image dimensions
    for i in range(w):
        for j in range(h):
            if pixels[i, j] == (0, 0, 0):
                pixels[i, j] = (255, 255, 255)


def main():
    """Solve challenge 5: CAPTCHA me if you can."""
    # Load requests session
    session = requests.Session()
    while True:
        page = session.get(URL)
        # Load image
        img = base64_to_image(get_image_string(page.text))
        # Clean it up
        remove_black(img)
        # Get captcha text using OCR and remove non-ASCII characters
        text = pytesseract.image_to_string(img)
        text = re.sub('\W', '', text)
        # Send solution and get response
        print("Trying solution: " + text)
        data = {'cametu': text}
        resp = session.post(URL, data=data)
        soup = BeautifulSoup(resp.text, 'html5lib')
        msg = soup.p.text
        # If there's no losing message, we got it! Print html page for code
        if 'chance' not in msg:
            print("Winner winner chicken dinner")
            print(soup)
            return

        # If we failed, wait 3 seconds for new captcha to appear
        sleep(3)


if __name__ == "__main__":
    main()
