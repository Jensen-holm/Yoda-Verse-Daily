import requests

URL = "https://yodish.p.rapidapi.com/yoda.json"

headers = {
    "X-RapidAPI-Key": "cd29d7a075mshb08572d8da1b1b4p153cd5jsn416ef45e8580",
    "X-RapidAPI-Host": "yodish.p.rapidapi.com"
}


def translate(text: str) -> str:
    r = requests.request(
        "POST",
        URL,
        headers=headers,
        params={
            "text": text,
        }
    )
    return r.text


if __name__ == "__main__":
    test = "For the grace of God has appeared that offers salvation to all people."
    print(translate(test))
