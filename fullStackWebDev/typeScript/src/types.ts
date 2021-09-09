// simple data types
let myString: string;
let myNum: number;
let myBool: boolean;
let myVar: any

myString = "hello World" + " god help me with web dev";
myString = 'Hello'.slice(0,3) //indexing
myNum = 22; // hexadeicmal e.g. 0xff2 works fine
myBool = false;

myVar = 23
myVar = 'hello'
console.log(myString);
console.log(myNum);

//Arrays (defining method one)
let strArr: string[]
let numArr: number[]
let boolArr: boolean[]

strArr = ['Hello', 'World'];
numArr = [12,123]
boolArr = [true, false]

console.log(strArr)

//Arrays (method 2)
let strArr2: Array<string>
let numArr2: Array<string>

//tupple
let strNumTuple: [string, number] // doesn't let you add more than the two defined types

strNumTuple = ['je', 23]

// void, undefined and null
// https://www.typescriptlang.org/docs/handbook/release-notes/typescript-2-0.html
