import express from "express";
import { ApolloServer } from "apollo-server-express";
import { typeDefs } from "./schema/typeDefs";
import { resolvers } from "./schema/resolvers";
import { __prod__ } from "./constants";
import { User } from "./entity/user";
import "reflect-metadata";
import { createConnection } from "typeorm";

async function startApolloServer() {
    const server = new ApolloServer({ typeDefs, resolvers });
    await server.start();

    const app = express();
    const PORT: string | number = process.env.PORT || 4000;

    app.use(express.static(__dirname + "/../public/"));
    app.use("*/dist", express.static(__dirname + "/../dist/"));

    app.get("/", (req, res) => {
        res.sendFile("index.html");
    });

    server.applyMiddleware({ app });

    await new Promise((resolve) => app.listen({ port: PORT }, resolve));
    console.log();
    return { server, app };
}

startApolloServer();
createConnection()
    .then(async (connection) => {
        console.log("Inserting a new user into the database...");
        const user = new User();

        user.firstName = "Timber";
        user.lastName = "chad@chad";
        user.age = 56;

        await user.save();

        console.log("User Created");
    })
    .catch((error) => console.log(error));
