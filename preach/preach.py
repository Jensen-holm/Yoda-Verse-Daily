import requests
import json
import os

URL = "https://you-chat-gpt.p.rapidapi.com/"

HEADERS = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "cd29d7a075mshb08572d8da1b1b4p153cd5jsn416ef45e8580",
    "X-RapidAPI-Host": "you-chat-gpt.p.rapidapi.com"
}


def prompt(person: str) -> str:
    return f"tell me a bible verse as if you are {person} and " \
           "then tell me the chapter and verse it would be in the bible"


def center_multiline_output(string: str) -> None:
    cols, _ = os.get_terminal_size()
    for thing in string.split("\n"):
        print(thing.center(cols))


def preach(person: str):
    payload = {
        "question": prompt(person),
        "max_response_time": 100,
    }

    r = requests.request(
        "POST",
        URL,
        json=payload,
        headers=HEADERS,
    )

    data = json.loads(r.text)
    if not data["answer"]:
        return data["warning"]
    return data["answer"]


if __name__ == "__main__":
    preach("yoda")
