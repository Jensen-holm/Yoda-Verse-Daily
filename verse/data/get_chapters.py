from bs4 import BeautifulSoup
from book import Book
import requests

URL = "http://home.snu.edu/~hculbert/chapters.htm"


def get_chapters():
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, features="lxml")
    ol = soup.find_all("ol")[0]

    books = []
    for book in ol:
        print(book)

    return


if __name__ == "__main__":
    get_chapters()
