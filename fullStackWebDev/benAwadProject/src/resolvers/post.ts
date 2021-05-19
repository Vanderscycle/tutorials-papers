// graphql you create a class and decorate
import { Resolver, Query, Ctx } from "type-graphql";
import { Post } from "../entities/post";
import { MyContext } from "../types"
// because the entity we are passing is not a graphQL type we need to transform it.
// the neat thing with graphql is that since Post is a class we can transform it into a graphql type
//
@Resolver()
export class PostResolver {
    // if you do not export the class you will not be able see it when importing from another file
    @Query(() => [Post]) // array [] of type Post // setting graphql type 
    posts(@Ctx() {em}: MyContext): Promise<Post[]> {  //ctx or {em} destructure // also setting typescript type
        return em.find(Post, {})
    }
}
