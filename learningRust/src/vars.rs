//need mut
//Rust is block scoped eg defined vars in a function only exist in that function
pub fn run() {
    let name = "Brad";
    let mut age = 69; //gives us a warning because we never used the var prior change
    age = 420;
    println!("My name is {} and I am {}", name, age);

    //const keyword
    const ID: i32 = 001;
    println!("ID: {}", ID);

    //assign multiple variables at once
    let (myName, myAge) = ("Brad", 69);
    println!("{} is {}", myName, myAge)
}
