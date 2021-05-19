//https://mikro-orm.io/docs/defining-entities
import { Entity, PrimaryKey, Property } from "@mikro-orm/core";
import { ObjectType, Field, Int} from "type-graphql" // because we need to set the type for some fields (date, ints) we import 
// WARN: Int comes from typegraphql but string doesn't ?

@ObjectType() // we can stack decorators
@Entity()
export class Post {

    @Field(() => Int) // to add a field to each ones
    @PrimaryKey()
    id!: number;

    @Field(() => String) // WARN: if there is a field I do not want to expose then  do not add Field decorator
    @Property() // {type: "date"}
    createdAt: Date = new Date();
    

    @Field(() => String) // 
    @Property({ onUpdate: () => new Date() })
    updatedAt: Date = new Date();

    @Field()
    @Property({type: 'text'})
    title!: string;
}
