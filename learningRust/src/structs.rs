// Structs - Used to create custom data types

// traditional struct
struct Color {
    // u8 because its 0 -> 255struct Color {
    red: u8,
    green: u8,
    blue: u8,
}

struct Person {
    first_name: String,
    last_name: String,
}

impl Person {
    // Construct person
    fn new(first: &str, last: &str) -> Person {
        Person {
            first_name: first.to_string(),
            last_name: last.to_string(),
        }
    }

    // Get full name
    fn full_name(&self) -> String {
        format!("{} {}", self.first_name, self.last_name)
    }

    // Set last name
    fn set_last_name(&mut self, last: &str) {
        self.last_name = last.to_string();
    }

    // Name to tuple
    fn to_tuple(self) -> (String, String) {
        (self.first_name, self.last_name)
    }
}

pub fn run() {
    let mut c = Color {
        red: 234,
        green: 79,
        blue: 78,
    };
    c.red = 200;
    println!("Color: {} {} {}", c.red, c.green, c.blue);
    let mut p = Person::new("Mary", "Doe");
    println!("Person {}", p.full_name());
    p.set_last_name("Williams");
    println!("Person {}", p.full_name());
    println!("Person Tuple {:?}", p.to_tuple());
}
