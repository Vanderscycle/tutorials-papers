// it looks like the class is being run dirrectly, but what happens is that the class is wrapped in a module wrapper function
//prrof
//console.log(__dirname,__filename)
export class Person {
    //field (without it it works but TS yells at you)
    name: string;
    age: number;

    //constructor
    constructor(name: string, age: number) {
        this.name = name;
        this.age = age;
    }
    greeting() {
        console.log(`My name is ${this.name} and I am ${this.age}`) //JS uses backticks for "f" strings
    }
}
// export const person = {
//     name: 'Jonh Doe',
//     age: 30
// }
// instead you can also export using:
// module.exports = person // I prefer to add export to the class or variable. (makes it clearer)
