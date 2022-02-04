//no turnary operators in rust T_T
pub fn run() {
    let age: i32 = 18;
    let mut checkID: bool = false;
    let knowsPErsonAge = true;

    //IF/ELSE
    if age >= 21 && (checkID || knowsPErsonAge) {
        println!("Bartender: what would you like to drink?")
    } else if age < 21 && checkID {
        println!("Bartender: Sorry no beer for you ")
    } else {
        println!("Bartender: Multi-pass please");
        checkID = true;
        println!("Bartender: checkID status: {}", checkID);
    }

    //Shorthand IF
    let isOfAge: bool = if age >= 21 { true } else { false };
    println!("Is of Age: {}", isOfAge);
}
