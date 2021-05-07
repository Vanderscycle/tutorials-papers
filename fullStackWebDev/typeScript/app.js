function combine(input1, input2) {
    var result;
    if (typeof input1 === "number" && typeof input2 === "number") { //numbers only
        result = input1 + input2;
    }
    else { //strings only
        result = input1.toString() + input2.toString();
    }
    return result;
}
var combineAges = combine(30, 20);
console.log(combineAges);
var combineNames = combine("bob", "margaret");
console.log(combineNames);
