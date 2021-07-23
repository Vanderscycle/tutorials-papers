import { Resolver, Query } from '@nestjs/graphql';


@Resolver()
export class UserResolver {


  @Query(()=> String)
  async users() {
    return 'hello world'
  }
}
