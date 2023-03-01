package biblical_yoda

import (
	"bytes"
	"fmt"
	"io/ioutil"
	"net/http"
)

const (
	URL     = "https://you-chat-gpt.p.rapidapi.com/"
	PAYLOAD = `{
    "question": "Select a random bible verse and translate it into yoda speak",
    "max_response_time": 30
}`
)

func Preach() (string, error) {

	payload := bytes.NewBuffer([]byte(PAYLOAD))

	req, _ := http.NewRequest(
		"POST",
		URL,
		payload,
	)

	req.Header.Add("content-type", "application/json")
	req.Header.Add("X-RapidAPI-Key", "cd29d7a075mshb08572d8da1b1b4p153cd5jsn416ef45e8580")
	req.Header.Add("X-RapidAPI-Host", "you-chat-gpt.p.rapidapi.com")

	res, err := http.DefaultClient.Do(req)
	if err != nil {
		return "", fmt.Errorf("error in spiritual yoda request: %v", err)
	}

	defer res.Body.Close()
	body, err := ioutil.ReadAll(res.Body)
	if err != nil {
		return "", fmt.Errorf("error reading response body: %v", err)
	}

	return string(body), nil
}