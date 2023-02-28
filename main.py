import datetime
import requests


DATE = datetime.datetime.now() 
URL = "https://ajith-holy-bible.p.rapidapi.com/GetVerses"
HEADERS = {
	"X-RapidAPI-Key": "cd29d7a075mshb08572d8da1b1b4p153cd5jsn416ef45e8580",
	"X-RapidAPI-Host": "ajith-holy-bible.p.rapidapi.com"
}


def get_verse(qs: str):
    try:
        return requests.request(
                "GET", 
                URL, 
                headers=HEADERS, 
                params=qs,
        ).text
    except requests.ConnectionError or requests.HTTPError as e:
        raise(f"Error Sending api request for biblical data.")


def main():
    querystring = {"Verse":"1","chapter":"1","Book":"Luke"}
    return get_verse(qs=querystring)


if __name__ == "__main__":
    print(main())

