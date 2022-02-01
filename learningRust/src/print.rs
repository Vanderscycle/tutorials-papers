pub fn run() {
    //print to console
    println!("Hellow from print.rs");

    //formatted strings
    println!("Number: {}", 1);

    // Positional ARguments
    println!(
        "{0} is from {1} and {0} likes to {2}",
        "brad", "Mass", "code"
    );

    //Named Arguments
    println!(
        "{name} likes to play {activity}",
        name = "john",
        activity = "Baseball"
    );

    //Placeholder traits
    println!("Binary: {:b} Hex: {:x} OCtal: {:o}", 10, 10, 10);

    //Placeholder for debug trait
    println!("{:?}", (12, true, "hello"));

    //basic math
    println!("10 + 10 = {}", 10 + 10)
}
