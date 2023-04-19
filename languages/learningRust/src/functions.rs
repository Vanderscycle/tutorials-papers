pub fn run() {
    greeting("Hello", "Jane");

    //bind function values to variables
    let getSum = add(5, 5);
    println!("Sum: {}", getSum);

    //closure
    let n3: i32 = 10;
    let addNums = |n1: i32, n2: i32| n1 + n2 + n3; //INFO: can also use outside variables
    println!("C Sum: {}", addNums(3, 3));
}

fn greeting(greet: &str, name: &str) {
    println!("{} {}, nice to meet you", greet, name)
}

fn add(n1: i32, n2: i32) -> i32 {
    //no semicolons means the returb (I'd like something mroe explicit tho :/)
    n1 + n2
}
