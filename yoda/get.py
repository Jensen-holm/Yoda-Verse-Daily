import requests
from verse.error import is_error, error_message

URL = "http://yodaspeak.org/"


def translate(data) -> str:
    r = requests.request(
        "POST",
        URL,
        data=data,
    )
    if is_error(r):
        raise error_message(URL, r.status_code)
    return r.text


if __name__ == "__main__":
    test = "For the grace of God has appeared that offers salvation to all people."
    data = {"text": test}
    print(translate(data))
