from bs4 import BeautifulSoup
import requests
import os


URL = "http://home.snu.edu/~hculbert/chapters.htm"


def get_chapters():
    r = requests.get(URL)
    soup = BeautifulSoup(r.text, features="lxml")
    ol = soup.find_all("ol")

    books = {}
    for li in ol:
        print(li)

    return books


if __name__ == "__main__":
    print(get_chapters())
