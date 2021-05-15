function add(n1, n2) {
    return +n1 + +n2;
}
function printResult(num) {
    console.log("Result: " + num);
    // if you were to add return with nothing you would be undefined which is a value in JS
    // you can set the function return type to be undefined but you will need a empty return
}
printResult(add(5, 12));
var combineValues = add; //pointer to a function
console.log(combineValues(8, 8));
// TODO hello 

