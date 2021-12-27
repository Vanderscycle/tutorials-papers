//functions
function getSum(num1: number, num2: number): number {
  //return type
  return num1 + num2;
}

console.log(getSum(1, 4));

let mySum = function (num1: any, num2: number): number {
  if (typeof num1 == "string") {
    num1 = parseInt(num1);
  }

  if (typeof num1 == "string") {
    num1 = parseInt(num1);
  }

  return num1 + num2;
};
console.log(mySum("test", 5));

// lastname? is an optional parameter and will be undefined if no value is assigned
// default value can be given e.g. firstname: string = 'bob'
function getName(firstName: string = "bob", lastname?: string): string {
  if (lastname == undefined) {
    return firstName;
  }
  return firstName + " " + lastname;
}

console.log(getName("john"));
console.log(getName());

function myVoid(): void {
  return;
}
