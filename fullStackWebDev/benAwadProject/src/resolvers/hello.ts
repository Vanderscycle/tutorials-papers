// graphql you create a class and decorate
import {Resolver, Query} from 'type-graphql'

@Resolver()
export class HelloResolver {// if you do not export the class you will not be able see it when importing from another file
    @Query(() => String )// need to define what the query returns
    hello(){
        return "hello world"
    }
    
    @Query(() => String )// need to define what the query returns
    bye(){
        return "bye"
    }
} 
