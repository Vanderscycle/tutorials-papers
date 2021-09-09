import { __prod__ } from "./constants";
import { Post } from "./entities/post";
import { MikroORM } from "@mikro-orm/core";
import path from 'path';

console.log("dirname:", __dirname);// abs path to the file being called
export default {
    migrations: {
        path: path.join(__dirname, './migrations'), // path to the folder with migrations
        pattern: /^[\w-]+\d+\.[tj]s$/, // regex pattern for the migration files (modified for TS and JS)
        disableForeignKeys: false, //https://github.com/driescroons/mikro-orm-graphql-example/issues/3
    },
    dbName: "benawad",
    entities: [Post],
    user: "",
    password: "",
    type: "postgresql",
    debug: !__prod__, //really cool way to not repeat ourselves
    //specify the type in parameters
} as Parameters<typeof MikroORM.init>[0]; //Parameters returns an array but we want the first element
// as const //casting so that type is not string but postgresql (intermediate)
