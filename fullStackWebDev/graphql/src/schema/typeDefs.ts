import { gql } from 'apollo-server-express'

export const typeDefs = gql`
  type User {
    name: String!
    age: Int!
    married: Boolean!
  }

  # Queries (all queries must go here)
  type Query {
    getAllUsers: [User!]!
  }
  # mutations
  type Mutation {
    createUser(name:String!, age:Int!, married: Boolean!): User!
  }

  `

