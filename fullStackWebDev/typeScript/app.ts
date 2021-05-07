//union types
function combine(input1: number | string, input2: number | string) {
    let result;
    if (typeof input1 === "number" && typeof input2 === "number") {//numbers only
        result = input1 + input2;
    } else {//strings only
        result = input1.toString() + input2.toString()
    }
    return result;
}
const combineAges = combine(30, 20);
console.log(combineAges);

const combineNames = combine("bob", "margaret");
console.log(combineNames);
