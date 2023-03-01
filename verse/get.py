import requests
from verse.error import is_error

URL = "https://ajith-holy-bible.p.rapidapi.com/GetVerses"
HEADERS = {
    "X-RapidAPI-Key": "cd29d7a075mshb08572d8da1b1b4p153cd5jsn416ef45e8580",
    "X-RapidAPI-Host": "ajith-holy-bible.p.rapidapi.com"
}


def get_verse(qs: dict[str, str]):
    """
    requests the Holy Bible API with the given
    query string as an argument
    :param qs: query string
    :return: text response from the api
    """
    r = requests.request(
        "GET",
        URL,
        headers=HEADERS,
        params=qs,
    )

    # check for errors in the request
    if is_error(r):
        raise f"Error calling the api to get bible verse."
    return r.text