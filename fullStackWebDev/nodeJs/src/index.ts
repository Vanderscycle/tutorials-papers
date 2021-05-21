console.log("Hello World");
// acceptable import method
//const person = require('./person')
//console.log(person)

// better import method
import { Person } from "./person"; //funny thing, node doesn't support import but since TS converts to JS we have no such issue
const person = new Person("Bro", 69);
person.greeting();
