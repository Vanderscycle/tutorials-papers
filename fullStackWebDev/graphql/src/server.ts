import express from "express";
//https://github.com/apollographql/apollo-server/tree/main/packages/apollo-server-express
import { ApolloServer } from "apollo-server-express"
import { resolvers } from "./schema/resolvers"
import { typeDefs } from "./schema/typeDefs"


async function startApolloServer() {
  // Construct a schema, using GraphQL schema language
  const server = new ApolloServer({ typeDefs, resolvers });
  await server.start();

  const app = express();
  const PORT: string | number = process.env.PORT || 4000;

  app.use(express.static(__dirname + "/../public/"));
  app.use("*/dist",express.static(__dirname + "/../dist/"));

  app.get("/", (req, res) => {
    res.sendFile("index.html");
  });


  server.applyMiddleware({ app });

  await new Promise(resolve => app.listen({ port: PORT }, resolve));
  console.log(`🚀 Server ready at http://localhost:4000${server.graphqlPath}`);
  return { server, app };
}

startApolloServer()
