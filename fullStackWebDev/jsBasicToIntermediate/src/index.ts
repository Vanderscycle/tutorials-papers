//references
//https://www.typescriptlang.org/docs/handbook/2/basic-types.html
//https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide

console.log("Please work");
// variables available in JS/TS var (global), let, const (block)

let ages: number = 30;
ages = 32; //const wouldn't allow to reassign the value later, but you can still change through methods

console.log(ages);

//primitive datatype (direstly assigned to memory)
//string, number, boolean, null, undefined, symbol (ES6)
const names: string = "john";
const age: number = 31;
const rating: number = 4.5; //no float or int in JS/TS only
const isCool: Boolean = true;
const x: null = null; // typeof x return null (because of the first implementation of JS) and that's not true
const u: undefined = undefined; //const must always be initialized only let
let z; // undefined by default

console.log(typeof x);

//concatenation
//console.log("my name" + names + "...")
//Template String
const hello: string = `My name is ${names} and I am ${age}`;
console.log(hello);

//string propreties and method
const s: string = "hello World!";
console.log(s.length);
//console.log(s.toLowerCase())//method to lower all
console.log(s.substring(0, 5).toUpperCase()); //just like py you can chain them

console.log(s.split(" ")); //string to array
/*
multiline of comments
*/
//Arrays - variable that hold multiple values (const prefered)
//https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Array
//using a constructor (old method)
const numbers: Array<number> = new Array(1, 2, 3, 4, 5);
console.log(numbers);
//more modern method (notice the different type assignement for arrays)
const fruits: (string | number | boolean)[] = [
  "apples",
  "oranges",
  "pears",
  10,
  true,
];
fruits.push("mangos"); // append a value to the end of the array
fruits.unshift("strawberries"); //inser a value at the beginning of the array
console.log(fruits[1]); //0 indexed thanks goodness
console.log(fruits);
let singleFruit = fruits.pop();
console.log(`pop'd item ${singleFruit}`);
console.log(Array.isArray(fruits));
console.log(fruits.indexOf("oranges")); //super important method

//oject litterals w/ TS interfaces
interface Person {
  firstName: string;
  lastName: string;
  age: number;
  email?: string; //optional parameter
  hobbies: Array<string>;
  address: any; //idk what to call {}
}

const person: Person = {
  firstName: "john",
  lastName: "Bro",
  age: 31,
  hobbies: ["JS", "python", "getting rejected for jobs"],
  address: {
    street: "50 main st",
    city: "Broton",
    state: "Swole",
  },
};
console.log(
  person.firstName,
  person.lastName,
  `fav hobbies ${person.hobbies[1]}`
);
//if you want popups use alert()
//if you want to destructure
const {
  firstName,
  lastName,
  address: { city },
} = person; //works for nested components but don't forget the ":"
console.log(firstName);
person.email = "swoleTow@thic.com";

console.log(person);

//arrays of objects
interface TodoList {
  id: number;
  text: string;
  isCompleted: boolean;
}
// extending the Array interface
interface TodoList extends Array<TodoList> {}
const todos: TodoList[] = [
  {
    id: 1,
    text: "broooo",
    isCompleted: true,
  },
  {
    id: 2,
    text: "broooo out with the wife",
    isCompleted: false,
  },
  {
    id: 3,
    text: "workout",
    isCompleted: true,
  },
];
console.log(todos[1]);
//honestly need more time to think about the encoding/decoding of json
//https://stackoverflow.com/questions/29705211/object-defineproperty-on-a-prototype-prevents-json-stringify-from-serializing-it
//http://choly.ca/post/typescript-json/
const todoJson = JSON.stringify(todos);
console.log(todoJson);

//for loops
for (let i = 0; i < 3; i++) {
  console.log(i);
}
//while loop (variable set outside the loop)
let i = 0;
while (i <= 1) {
  console.log(`while loop number ${i}`);
  i++;
}
//loop through arrays
for (let cursor in todos) {
  //of passes the item
  console.log(todos[cursor].text);
}
// forEach, map (create new array from array), filter (create new array based on a condition)
// better w/ arrow functions
todos.forEach(function (todo) {
  console.log(todo.id);
});
//loop through and only return an array of text (w/ arrow functions)
const todoText: string[] = todos.map((todo) => {
  return todo.text;
});
console.log(todoText);
const todoCompleted: string[] = todos // if filter only then assing TodoList[] as type
  .filter((todo) => {
    return todo.isCompleted === true;
  })
  .map((todo) => {
    return todo.text;
  });
console.log(todoCompleted);
// conditionals
const xNum: number = 10;
//=== datatype and value (prefer to use ===)
if (xNum === 10) {
  console.log("x is 10");
} else if (xNum > 10) {
  console.log("greater than 10");
} else {
  console.log("x is less than 10");
}
// or || and &&
// turnary operators
const color: string = xNum > 10 ? "red" : "blue";
console.log(color);
// switches
switch (color) {
  case "red":
    console.log("color is red");
    break;
  case "blue":
    console.log("color is blue");
    break;
  default:
    console.log("color is not red or blue");
    break;
}

//functions
function addNums(nums1: number, nums2: number = 2): void {
  //check whether a number is an integer
  console.log(Number.isInteger(nums1));
  console.log(nums1 + nums2);
}
// doesn't quite work :(
const addNum2 = (nums1: number, nums2: number = 2, nums3?: number): number => {
  if (nums3 == undefined) {
    return nums1 + nums2;
  } else {
    return nums1 + nums2 + nums3;
  }
};

addNums(1.5);
console.log(addNum2(1.2));
//object oriented programming (w/ constructor functions or classes)
//constructor function (do not use in TS)
/*
function Person (firstName: string, lastName:string, dob: string) {
    this.firstName = firstName
    this.lastName = lastName
    this.dob = dob
}
//instantiate obj
const person1 = new Person('John', 'asdj','2019-2-1')
console.log(person1);
*/
interface PersonClass {
  firstName: string;
  lastName: string;
  dob: Date;
  getBirthYear(): string;
  getFullName(): string;
}
class Person2 implements PersonClass {
  //propreties
  firstName: string;
  lastName: string;
  dob: Date;
  //constructor
  constructor(firstName: string, lastName: string, dob: string) {
    this.firstName = firstName;
    this.lastName = lastName;
    //date object
    //https://www.javatpoint.com/typescript-date-object
    this.dob = new Date(dob);

    console.log(`person Created ${this.firstName} ${this.lastName}`);
  }
  getBirthYear(): string {
    return this.dob.getFullYear();
  }
  getFullName(): string {
    return `${this.firstName} ${this.lastName}`;
  }
}
const bro1 = new Person2("bro", "mongoose", "4-2-4269");
console.log(bro1.dob.getFullYear());
console.log(bro1.getBirthYear());
console.log(bro1.getFullName());
console.log(bro1);
