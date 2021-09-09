import { Resolver, Query } from "@nestjs/graphql";

@Resolver()
export class CatsResolver {
  // constructor(
  //   private authorsService: AuthorsService,
  //   private postsService: PostsService,
  // ) {}

  @Query(() => String)
  async hello() {
    return 'hallo'
  }
}

