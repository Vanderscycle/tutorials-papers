import "reflect-metadata";
import {createConnection} from "typeorm";
import {User} from "./entity/User";

createConnection().then(async connection => {

    console.log("Inserting a new user into the database...");
    const user = new User();

    user.name = "Timber";
    user.email = "chad@chad";
    user.role = 'admin';

    await user.save;

    console.log("User Created");

}).catch(error => console.log(error));
