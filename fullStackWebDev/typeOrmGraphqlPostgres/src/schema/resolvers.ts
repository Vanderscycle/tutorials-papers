import { Resolver, Query, Mutation, Arg } from "type-graphql";
import { User } from '../entity/user'

@Resolver()
export class resolvers  {
  @Query(() => String)
  hello() {
    return "world";
  }
  //findall
  @Query(() => [ User ])
  async getAllUsers() {
    return await User.find()
  }
  //findone
  @Query(() => User)
  user(@Arg("id") id: number) {
    return User.findOne({ where: { id }});
  }
  //CREATE
  @Mutation(() => User )
  async createNewUser(
    @Arg('firstName') firstName:string,
    @Arg('lastName') lastName:string,
    @Arg('age') age:number): Promise<User> {
    const newUser = User.create({firstName, lastName, age})
    await newUser.save()
    return newUser
  }
  //UPDATE
  @Mutation(() => User)
  async updateUser(
    @Arg("id") id: number,
    @Arg('firstName', { nullable: true }) firstName:string,
    @Arg('lastName', { nullable: true }) lastName:string,
    @Arg('age', { nullable: true }) age:number): Promise<User> {
    const user = await User.findOne({ where: { id }});

    if (!user) {
      throw new Error(`The user with id: ${id} does not exist!`);
    }

    Object.assign(user, {firstName, lastName, age});
    await user.save();

    return user;
  }
  //DELETE
  @Mutation(() => Boolean)
  async deleteUser(
    @Arg("id") id: number,
  ):Promise<Boolean> {
  const user = await User.findOne({ where: { id }});

  if (!user) {
    throw new Error(`The user with id: ${id} does not exist!`);
  }
  await user.remove();
  return true;

  }
};
