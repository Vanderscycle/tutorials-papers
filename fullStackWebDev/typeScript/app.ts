function add(n1: number, n2: number): number {
    //normally typescript will infer the type
    return +n1 + +n2;
}

function printResult(num: number): void {
    //could add :void but JS doesn't have a void type
    console.log("Result: " + num);
    // if you were to add return with nothing you would be undefined which is a value in JS
    // you can set the function return type to be undefined but you will need a empty return
}
//callbacks
function addAndHandle(n1: number, n2: number, cb: (num: number) => void) {
    //anything you might return will not be used
    const result = n1 + n2;
    cb(result);
}
printResult(add(5, 12));

let combineValues: (a: number, b: number) => number; //Can take anyfunction that has two input as number
//let combineValues: Function //assign a type
combineValues = add; //pointer to a function
//combineValues = printResult // doesn't fit
//combineValues = 5 //error
console.log(combineValues(8, 8));

addAndHandle(10, 20, (result) => {
    console.log(result); //result is an anonymous function (lambda)
});
