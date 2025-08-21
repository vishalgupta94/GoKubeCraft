package main

import (
	"fmt"
	"io"
	"net/http"
	"strings"
	"sync"
)

func spend(money *int, mutex *sync.Mutex, wg *sync.WaitGroup) {
	for i := 0; i < 100000; i++ {
		mutex.Lock()
		*money -= 100
		mutex.Unlock()
	}

	wg.Done()
}

func earn(money *int, mutex *sync.Mutex, wg *sync.WaitGroup) {
	for i := 0; i < 100000; i++ {
		mutex.Lock()
		*money += 1000
		mutex.Unlock()
	}
	wg.Done()
}

const abcd = " abcdefghijklmnopqrstuvwxyz<>"

func main() {
	resp, err := http.Get("https://www.google.com")

	if err != nil {
		panic(err)
	}

	defer resp.Body.Close()

	data, err := io.ReadAll(resp.Body)

	if err != nil {
		panic(err)
	}

	for _, b := range data {
		fmt.Println(strings.Index(abcd, string(b)))
	}

	// fmt.Println(string(data))

}
