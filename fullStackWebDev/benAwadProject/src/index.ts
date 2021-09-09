import 'reflect-metadata'
import { MikroORM } from "@mikro-orm/core";
import { __prod__ } from "./constants";
//import { Post } from "./entities/post";
import microConfig from "./mikro-orm.config";
import express from "express";
import { ApolloServer } from "apollo-server-express";
import { buildSchema } from "type-graphql";
import { HelloResolver } from "./resolvers/hello";
import { PostResolver } from "./resolvers/post"
const main = async () => {
    // set-up DB connection
    const orm = await MikroORM.init(microConfig);
    orm.getMigrator().up(); //automaticallyrun the migrations
    // set-up express
    const app = express();
    const apolloServer = new ApolloServer({
        schema: await buildSchema({
            resolvers: [HelloResolver, PostResolver],
            validate: false,
        }), // returns a promise
        context: () => ({ em: orm.em })// context is a special object that is accessible by all resolvers, which can then access
    });

    apolloServer.applyMiddleware({ app }); // creates a graph ql endpoint

    app.listen(4000, () => {
        console.log("server started on localhost:4000");
    });
    // test express
    app.get("/", (_, res) => {
        res.send("hello");
    });

    // DB test
    // const post = orm.em.create(Post, { title: "My first post" });
    // await orm.em.persistAndFlush(post);
    // const posts = await orm.em.find(Post, {}) //gets all the posts in my db
    // console.log(posts)
};

main().catch((err) => {
    console.error(err);
});
