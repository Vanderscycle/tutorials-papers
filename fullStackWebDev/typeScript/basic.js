console.log("Your code goes here...!!!");
function add(n1, n2, showRes, phrase) {
    console.log(typeof number1);
    var result = n1 + n2;
    if (showRes) {
        console.log(phrase + result);
        // console.log(phrase + n1 + n2); // this way will reintroduce the concat bug we had earliers
    }
    else {
        return n1 + n2;
    }
}
var numberx; // bad practice let number1: number = 5 because TS will infer number
// although this is good if you init an empty var
var number1 = 5; //'5'+2.8=52.8
var number2 = 2.8;
var printResults = true;
var resultPhrase = "Result is: ";
var result = add(number1, number2, printResults, resultPhrase);
console.log(result);
