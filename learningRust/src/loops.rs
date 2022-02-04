pub fn run() {
    //let infinite loop
    let mut count: i32 = 0;
    //infinite Loop (jk)
    loop {
        count += 1;
        println!("Number :{}kl", count);
        if count == 5 {
            break;
        }
    }
    //while Loop FizzBuzz
    while count <= 100 {
        if count % 15 == 0 {
            println!("FizzBuzz");
        } else if count % 3 == 0 {
            println!("fizz");
        } else if count % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", count)
        }
        count += 1
    }

    for count in 0..100 {
        if count % 15 == 0 {
            println!("FizzBuzz");
        } else if count % 3 == 0 {
            println!("fizz");
        } else if count % 5 == 0 {
            println!("buzz");
        } else {
            println!("{}", count)
        }
    }
}
