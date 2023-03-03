import requests


URL = "https://you-chat-gpt.p.rapidapi.com/"

PROMPT = "Pick a ranodm bible verse, and translate it into how yoda from star wars would say the bible verse. Only tell me the way yoda would say it and the location of the bible verse and nothing else"

PAYLOAD = {
	"question": PROMPT,
	"max_response_time": 30
}

HEADERS = {
	"content-type": "application/json",
	"X-RapidAPI-Key": "cd29d7a075mshb08572d8da1b1b4p153cd5jsn416ef45e8580",
	"X-RapidAPI-Host": "you-chat-gpt.p.rapidapi.com"
}


def preach_yoda():
    try:
        r = requests.request(
            "POST",
            URL,
            json=PAYLOAD,
            headers=HEADERS,
        )
        return r.text

    except:
        return f"error in post request"

if __name__ == "__main__":

    print(preach_yoda())

