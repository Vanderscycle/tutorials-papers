import { Resolver, Query } from "type-graphql";
import { User } from '../entity/user'

@Resolver()
export class resolvers  {
  @Query(() => String)
  hello() {
    return "world";
  }
  @Query(() => [User])
  getAllUsers() {
    return User.find()
  }
    
};
