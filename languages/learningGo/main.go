package main

import (
	"fmt" //format strings and print in the console
	"math"
	"sort"
	"strings"
)

func main() {
	fmt.Println("hello World")
	// lesson12()
}
func lesson12() {
	//maps (or object in javascript / dict)
	// all of the keys in a map must have the same type(float/int/string)
	//same for the keys
	menu := map[string]float64{
		"soup":           4.99,
		"pie":            7.99,
		"shala":          6.98,
		"toffee puddung": 3.55}
	fmt.Println(menu)
	fmt.Println(menu["pie"])
	//loop maps
	for k, v := range menu {
		fmt.Printf("%v - %v \n", k, v)
	}
	phoneBook := map[int]string{
		12381414: "mario",
		12314159: "luigi",
		12385322: "peach"}
	fmt.Println(phoneBook)
	fmt.Println(phoneBook[12381414])

	phoneBook[12381414] = "bowsewr"
	fmt.Println(phoneBook)

	phoneBook[12314159] = "yoshi"
	fmt.Println(phoneBook)

}

// func lesson11() {
// 	//WARN: additional lesson can be found in goModule
// 	//package scope and func imports
// 	//https://golang.org/doc/tutorial/call-module-code
// 	for _, v := range points {
// 		fmt.Println(v)
// 	}
// 	Test()

// }

func lesson10() {
	//functions (multiple return)
	fmt.Println("functions (multiple returns)")
	res, res2 := getInitials("tifa lockhart")
	fmt.Println(res, res2)
}

func getInitials(n string) (string, string) {
	n = strings.Title(n)
	var arrayResult [2]string = [2]string{"", ""}
	stringArray := strings.Split(n, " ")
	for index, value := range stringArray {
		//fmt.Println(value[:1], index)
		arrayResult[index] = value[:1] //could have also created an empty object (w/make) and appended

	}
	return arrayResult[0], arrayResult[1]
}

func lesson9() {
	//functions
	fmt.Println("functions")

	cycleNames([]string{"cloud", "tifa", "barret"}, sayGreeting)
	cycleNames([]string{"cloud", "tifa", "barret"}, sayBye)
	a1 := circleArea(10.5)
	a2 := circleArea(12)
	fmt.Println(a1, a2)
	fmt.Printf("cicle 1 is %0.3f and circle 2 is %0.3f\n", a1, a2)
}
func sayGreeting(n string) {
	fmt.Printf("good morning %v \n", n)
}
func sayBye(n string) {
	fmt.Printf("goodbye %v \n", n)
}

// takes a string array and a function
func cycleNames(n []string, f func(string)) {
	for _, v := range n {
		f(v)
	}
}

func circleArea(r float64) float64 {
	return math.Pi * math.Exp2(r)
}

func lesson8() {
	//bool and conditions
	fmt.Println("bool and conditions")

	age := 45
	fmt.Println(age <= 50)
	fmt.Println(age >= 50)
	fmt.Println(age == 45)
	fmt.Println(age != 50)

	//if statment
	if age < 30 {
		fmt.Println("age is less than 30")
	} else if age < 40 {
		fmt.Println("age is less than 40")
	} else {
		fmt.Println("age is greater than 40")
	}
	names := []string{"yoshi", "mario", "peach", "bowser", "luigi"}

	for index, value := range names {
		if index == 1 {
			fmt.Println("continuing at pos", index)
			continue //more like a skip
		}
		if index > 2 {
			fmt.Println("breaking at pos", index)
			break
		}
		fmt.Printf("the value at pos %v is %v\n", index, value)

	}

}
func lesson7() {
	//loooooooooooops
	fmt.Println("hello loops")
	//x := 0
	//for x < 5 {
	//	fmt.Printf("value of x is: %v\n", x)
	//	x++
	//}

	//better
	for i := 0; i < 5; i++ {
		fmt.Printf("value of x is: %v\n", i)
	}
	names := []string{"yoshi", "mario", "peach", "bowser", "luigi"}

	for i := 0; i < len(names); i++ {
		fmt.Println(names[i])
	}
	//for in
	for index, value := range names {
		fmt.Printf("the position at index %v is %v\n", index, value)
		value = "new String" //doesn't update the value in the og slice (local copy)
	}
	//in case you don't want the value or index use _ to discard
	//for _, value := range names {
	//	fmt.Printf("the value is %v\n", value)
	//}

}
func lesson6() {
	//std lib "string"
	greeting := "hello there friends"

	fmt.Println(strings.Contains(greeting, "hello"))
	fmt.Println(strings.ReplaceAll(greeting, "hello", "hi")) //return a new string (doesn't alter the old one)
	fmt.Println(strings.ToUpper(greeting))
	fmt.Println(strings.Index(greeting, "ll"))
	fmt.Println(strings.Split(greeting, " ")) //get a slice

	//the og values isn't changed
	fmt.Println("original string value =", greeting)

	// ints method
	ages := []int{45, 25, 30, 60, 50, 60, 70, 15}
	sort.Ints(ages) //method does alter the slice
	fmt.Println(ages)

	index := sort.SearchInts(ages, 30) //will be looking for the sorted array
	fmt.Println(index)
	index = sort.SearchInts(ages, 90) // return the len of the array
	fmt.Println(index == (len(ages)))
	fmt.Println(index)

	names := []string{"yoshi", "mario", "peach", "bowser", "luigi"}

	sort.Strings(names)
	fmt.Println(names)
	fmt.Println(sort.SearchStrings(names, "bowser"))

}

func lesson5() {
	//arrays and slices

	//arrays (cannot change the array size) go arrays are more like tupples
	//var ages [3]int = [3]int{20, 25, 30} //array of only ints with room for 3
	var ages = [3]int{20, 25, 30}

	names := [4]string{"yoshi", "mario", "peach", "bowser"}
	names[1] = "Luigi"

	fmt.Println(ages, len(ages))
	fmt.Println(names, len(names))

	//slices (use arrays under the hood)
	var scores = []int{100, 50, 60} //because there's no limit defined
	scores[2] = 25

	scores = append(scores, 85) //appends returns a new slice
	fmt.Println(scores, len(scores))

	//slice ranges
	rangeOne := names[1:3]  //1 is included but 3 isn't
	rangeTwo := names[2:]   //from index 2 till the end
	rangeThree := names[:3] // from the start to index 3(not included)
	fmt.Println(rangeOne, rangeTwo, rangeThree)

	rangeOne = append(rangeOne, "jojo")
	fmt.Println(rangeOne)
}

func lesson4() {
	//fmt lib
	age := 69
	name := "giga chad"
	//Print (doesn't add a new line)
	fmt.Print("hello,")
	fmt.Print("world,\n")
	fmt.Print("newLine,\n")
	// Println adds a new line
	fmt.Println("Hello ninjas!") //
	fmt.Println("Goodbye ninjas!")

	fmt.Println("my age is", age, "and my name is", name)
	//Printf (fromatted strings) %_ = format specifier
	fmt.Printf("my age is %v and my name is %v \n", age, name) //%v variable
	fmt.Printf("my age is %q and my name is %q \n", age, name) //%q quotes (doesn't work on int/float types)
	fmt.Printf("age is of type %T \n", age)                    //%T type
	fmt.Printf("you scored %0.2f points \n", 255.55)           //%0.xf rounding  float

	//Sprintf (save formatted strings)
	var str = fmt.Sprintf("my age is %v and my name is %v \n", age, name)
	fmt.Printf("the saved string is: %s", str)
	//more info https://pkg.go.dev/fmt@go1.17.2
}
func learningString() {
	//fmt.Println("Hello there")

	//variable definition ( can't change the type on its value)
	var nameOne string = "strings are double quotes only"
	var nameTwo = "Luigi" // like typescript there is type inference
	var nameThree string
	fmt.Println(nameOne, nameThree, nameTwo)
	fmt.Printf("nameThree = %T\n", nameThree) // %T type

	nameOne = "peach"
	nameThree = "bowser"
	fmt.Println(nameOne, nameThree, nameTwo) // fmt and nameOne has to be use (variables and packages)

	//cannot be declared outside function
	// create and immediately assign
	nameFour := "yoshi"
	fmt.Println(nameFour)

	//ints
	var ageOne int = 20
	var ageTwo = 30
	ageThree := 40

	fmt.Println(ageOne, ageTwo, ageThree)

	//bits & memory
	//https://golang.org/ref/spec#Numeric_types
	//var numOne int8 = 25 //int8 is -128 to 127 only anything exceeding that will be an error
	//var numTwo int8 = -128
	//var numThree uint = 128 //unsigned

	//var scoreOne float32 = 25.98
	//var scoreTwo float64 = 189234124
	//scoreThree := 1.5
}
