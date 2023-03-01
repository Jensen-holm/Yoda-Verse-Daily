package main

import (
	"fmt"
	"github.com/Jensen-holm/Yoda-Verse-Daily/biblical_yoda"
)

func main() {

	r, err := biblical_yoda.Preach()

	if err != nil {
		panic(err)
	}

	fmt.Println(r)

}
