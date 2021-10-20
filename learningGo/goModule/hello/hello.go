package main

//https://golang.org/doc/tutorial/call-module-code
import (
	"example.com/greetings"
	"fmt"
)

func main() {
	// Get a greeting message and print it.
	message := greetings.Hello("Gladys")
	fmt.Println(message)
}
