import requests

url = "https://yodish.p.rapidapi.com/yoda.json"

querystring = {"text":"Master Obiwan has lost a planet."}

headers = {
	"X-RapidAPI-Key": "cd29d7a075mshb08572d8da1b1b4p153cd5jsn416ef45e8580",
	"X-RapidAPI-Host": "yodish.p.rapidapi.com"
}

response = requests.request("POST", url, headers=headers, params=querystring)

print(response.text)
