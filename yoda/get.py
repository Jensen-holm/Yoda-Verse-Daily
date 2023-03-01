import requests

URL = "https://you-chat-gpt.p.rapidapi.com/"

HEADERS = {
    "content-type": "application/json",
    "X-RapidAPI-Key": "cd29d7a075mshb08572d8da1b1b4p153cd5jsn416ef45e8580",
    "X-RapidAPI-Host": "you-chat-gpt.p.rapidapi.com"
}


def translate(text: str):
    payload = {
        "question": f"Re-write this sentence as if yoda from star wars said it: '{text}'",
        "max_response_time": 15
    }

    r = requests.request(
        "POST",
        URL,
        json=payload,
        headers=HEADERS,
    )

    return r.text


if __name__ == "__main__":
    test = "For the grace of God has appeared that offers salvation to all people."
    print(translate(test))
