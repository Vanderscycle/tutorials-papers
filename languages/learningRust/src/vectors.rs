//info : https://doc.rust-lang.org/rust-by-example/primitives/array.html

//INFO: vectors arr resizeable arrays
use std::{mem, vec}; //otherwiese you have to use std::mem:...

pub fn run() {
    let mut numbers: Vec<i32> = vec![1, 2, 3, 4, 5];

    // Add on to the Vector
    numbers.push(5);
    numbers.push(69);
    println!("{:?}", numbers);

    //get single val
    println!("singel value: {}", numbers[0]);
    // println!("singel value: {}", numbers.0); //doesn't work :/

    //get vector length
    println!("singel value: {}", numbers.len());

    //Vector are stack allocated
    println!("array occupies: {} bytes", mem::size_of_val(&numbers));

    // get slice
    let slice: &[i32] = &numbers[0..2]; //last one not included
    println!("slice: {:?}", slice);

    //lopp through vector values
    for x in numbers.iter() {
        println!("number: {}", x);
    }

    //loop & mutate values
    //INFO: similar to how map works in JS/TS
    for x in numbers.iter_mut() {
        *x *= 2;
    }
    println!("numbers Vec {:?}", numbers)
}
