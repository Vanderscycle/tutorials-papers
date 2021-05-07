//const person: { // suboptimal TS notation
//    name: string,
//    age: number //you can also say age: 30 but then its a const
//} = {//TS notation
//object
var Role;
(function (Role) {
    Role[Role["ADMIN"] = 0] = "ADMIN";
    Role[Role["READ_ONLY"] = 1] = "READ_ONLY";
    Role[Role["AUTHOR"] = 2] = "AUTHOR";
})(Role || (Role = {})); //enum type (same as in python) only in TS
var person = {
    name: "bro",
    age: 31,
    hobbies: ["sports", "Cooking"],
    role: [2, "author"],
    permission: Role.ADMIN
};
console.log(person.name);
var favoriteActivity; //string array
favoriteActivity = ["sports"];
person.role.push("admin"); //TS exception to the tupple rule
//person.role[1] = 10 //returns an error
for (var _i = 0, _a = person.hobbies; _i < _a.length; _i++) {
    var hobby = _a[_i];
    //TS type inference detecting that hobby will be a string type
    console.log(hobby.toUpperCase());
}
console.log(person.role[1]);
