// Primitive str = Immutable fixed-length string somewhere in memory
// String = Growable, heap-allocated data structure - Use when you need to modify or own string data
pub fn run() {
    let hello = "Hello"; //immutable
    let mut hello2 = String::from("hello");

    //get Length
    println!("Length: {}", hello2.len());
    //Push char (single character)
    hello2.push('w');
    //Push string
    hello2.push_str("orld");

    println!("{}", hello2);

    //check if empty  (There's like a ton of 'em)
    println!("Is Empty {}", hello2.is_empty());
    // Contains
    println!("Contains 'World' {}", hello2.contains("World"));

    // Replace
    println!("Replace: {}", hello2.replace("World", "There"));

    // Loop through string by whitespace
    for word in hello2.split_whitespace() {
        println!("{}", word);
    }

    // Create string with capacity
    let mut s = String::with_capacity(10);
    s.push('a');
    s.push('b');

    // Assertion testing
    assert_eq!(2, s.len());
    assert_eq!(10, s.capacity());

    println!("{}", s);
}
