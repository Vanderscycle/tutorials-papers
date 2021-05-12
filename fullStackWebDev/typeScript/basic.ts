console.log("Your code goes here...!!!");
function add(n1: number, n2: number, showRes: Boolean, phrase: string) {
    console.log(typeof number1);
    const result = n1 + n2;
    if (showRes) {
        console.log(phrase + result);
        // console.log(phrase + n1 + n2); // this way will reintroduce the concat bug we had earliers
    } else {
        return n1 + n2;
    }
}
let numberx: number; // bad practice let number1: number = 5 because TS will infer number
// although this is good if you init an empty var
const number1 = 5; //'5'+2.8=52.8
const number2 = 2.8;
const printResults = true;
let resultPhrase = "Result is: ";
const result = add(number1, number2, printResults, resultPhrase);

