//const person: { // suboptimal TS notation
//    name: string,
//    age: number //you can also say age: 30 but then its a const
//} = {//TS notation
//object

enum Role {
    ADMIN,//can use ADMIN =5 which will index from there
    READ_ONLY,
    AUTHOR,
} //enum type (same as in python) only in TS
const person: {
    name: string;
    age: number;
    hobbies: string[];
    role: [number, string]; //we want to override TS type assignment
    permission: number;
} = {
    name: "bro",
    age: 31,
    hobbies: ["sports", "Cooking"], //array
    role: [2, "author"], //tupple
    permission: Role.ADMIN,
};
console.log(person.name);
let favoriteActivity: string[]; //string array
favoriteActivity = ["sports"];

person.role.push("admin"); //TS exception to the tupple rule
//person.role[1] = 10 //returns an error

for (const hobby of person.hobbies) {
    //TS type inference detecting that hobby will be a string type
    console.log(hobby.toUpperCase());
}
console.log(person.role[1]);
