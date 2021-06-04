import 'reflect-metadata'
import express from 'express'
import { ApolloServer } from 'apollo-server-express'
import { buildSchema } from 'type-graphql';

//import { typeDefs } from './schema/typeDefs'
import { resolvers } from './schema/resolvers'
import { init_db } from './database'
import { __prod__,__port__ } from './constants'

async function startApolloServer () {
  await init_db().catch((error) => console.log(error))
  console.log('Database created.');
  //check schema and how t add typeDefs
  const schema = await buildSchema({
    resolvers: [ resolvers ],
  });
  const server = new ApolloServer({ schema })
  await server.start()

  const app = express()

  app.use(express.static(__dirname + '/../public/'))
  app.use('*/dist', express.static(__dirname + '/../dist/'))

  app.get('/', (req, res) => {
    res.sendFile('index.html')
  })

  server.applyMiddleware({ app })

  await new Promise((resolve) => app.listen({ port: __port__ }, resolve))
  console.log()
  return { server, app }
}

startApolloServer()
