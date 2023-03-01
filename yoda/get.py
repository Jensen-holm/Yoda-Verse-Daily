import requests

URL = "https://you-chat-gpt.p.rapidapi.com/"

HEADERS = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "cd29d7a075mshb08572d8da1b1b4p153cd5jsn416ef45e8580",
    "X-RapidAPI-Host": "you-chat-gpt.p.rapidapi.com"
}


def translate_random_verse() -> str:
    """
    :return: a bible verse in yoda speech
    """
    payload = {
        "question": f"Pick a random bible verse and translate it into how yoda from star wars would say it",
        "max_response_time": 30,
    }
    r = requests.request(
        "POST",
        URL,
        json=payload,
        headers=HEADERS,
    )
    return r.text
