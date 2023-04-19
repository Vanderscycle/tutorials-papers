//info : https://doc.rust-lang.org/rust-by-example/primitives/array.html
use std::mem; //otherwiese you have to use std::mem:...

// ARryas - Fixed list where elements are the same data types (e.g. numpy arrays)
pub fn run() {
    let numbers: [i32; 5] = [1, 2, 3, 4, 5];

    //re-assing value
    numbers[2] = 20;

    println!("{:?}", numbers);

    //get single val
    println!("singel value: {}", numbers[0]);
    // println!("singel value: {}", numbers.0); //doesn't work :/

    //get array length
    println!("singel value: {}", numbers.len());

    //array are stack allocated
    println!("array occupies: {} bytes", mem::size_of_val(&numbers));

    // get slice
    let slice: &[i32] = &numbers[0..2]; //last one not included
    println!("slice: {:?}", slice);
}
