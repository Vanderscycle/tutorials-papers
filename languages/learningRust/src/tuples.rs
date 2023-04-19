//INFO: https://doc.rust-lang.org/rust-by-example/primitives/tuples.html
pub fn run() {
    let person: (&str, &str, i8) = ("Brad", "Mass", 37); //don't have to define the type but its a good habit I say

    // realyl cool way to access the index
    println!("{} is from {} and is {}", person.0, person.1, person.2); //INFO: you cannot use person[2] array only
}
