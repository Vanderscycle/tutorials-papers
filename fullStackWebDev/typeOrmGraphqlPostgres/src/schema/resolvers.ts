import { Resolver, Query, Mutation, Arg } from "type-graphql";
import { User } from '../entity/user'

@Resolver()
export class resolvers  {
  @Query(() => String)
  hello() {
    return "world";
  }
  @Query(() => [ User ])
  async getAllUsers() {
    return await User.find()
  }
  @Mutation(() => User )
  async createNewUser(
    @Arg('firstName') firstName:string,
    @Arg('lastName') lastName:string,
    @Arg('age') age:number): Promise<User> {
    const newUser = User.create({firstName, lastName, age})
    await newUser.save()
    return newUser

  }
};
