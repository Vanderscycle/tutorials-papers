import { gql } from "apollo-server-express"
// Construct a schema, using GraphQL schema language
export const typeDefs = gql`
  type User {
    firstName: String!
    lastName: String!
    age: Int!
}
  type HelloWorld {
    msg: String!
  }

# Queries
type Query {
  getAllUsers: [User!]!
  hello: HelloWorld!
}
`;
