use std::env;

pub fn run() {
    let args: Vec<String> = env::args().collect();
    let command = args[1].clone();
    let name: &str = "brad";
    let status: &str = "100%";
    // println!("args {:?}", command);

    if command == "hello" {
        println!("hi {}, how are you?", name);
    } else if command == "status" {
        println!("Status is {}", status);
    } else {
        println!("not a valid command")
    }
}
