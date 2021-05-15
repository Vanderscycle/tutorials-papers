//type aliases
type Combinable = number | string
type ConversionDescriptor = 'as-number' | 'as-text'
//union types
function combine(
    input1: Combinable,
    input2: Combinable,
    resultConversion: ConversionDescriptor
) {
    //not any string only these two strings
    let result;
    if (
        (typeof input1 === "number" && typeof input2 === "number") ||
        resultConversion === "as-number"
    ) {
        //numbers only
        result = +input1 + +input2;
    } else {
        //strings only
        result = input1.toString() + input2.toString();
    }
    //if (resultConversion === 'as-number') {
    //    return +result //converts to a number (+)
    //} else {
    //    return result;
    //}
    return result;
}
const combineAges = combine(30, 20, "as-number");
console.log(combineAges);

const combineNames = combine("bob", "margaret", "as-text");
console.log(combineNames);
