//interface for class
interface UserInterface {
    name: string;
    email: string;
    age: number;
    register();
    payInvoice();
}
class User implements UserInterface{
    //propreties w/ access modifiers (private, protected)
    name: string; // can only be used within the class
    email: string; // can't access outside the class (excluding class inheritance)
    public age: number;
    // runs when instantiating the class (init)
    constructor(name: string, email: string, age: number) {
        //this (this class)
        this.name = name;
        this.email = email;
        this.age = age;

        console.log("User Created " + this.name);
    }
    //method (can also use access modifier)
    register():void {
        console.log(this.name + " is now registered");
    }
    payInvoice(): void {
        console.log(`${this.name} paid invoice`);
    }
}

class Member extends User {
    id: number;

    constructor(id: number, name: string, email: string, age: number) {
        super(name, email, age);
        this.id = id;
    }

    payInvoice() {
        super.payInvoice();
    }
}
//alternative to class inheritance is composition com

let bobby = new User("bob booby", "bob@bob.com", 34);
bobby.register;
console.log(bobby.age);

let mike: User = new Member(1, "Mike Smithy", "smithy@McSmithy.com", 56);
mike.payInvoice();
