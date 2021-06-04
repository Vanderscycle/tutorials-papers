import {Entity, PrimaryGeneratedColumn, Column, BaseEntity} from "typeorm";
import { ObjectType, Field, ID } from "type-graphql";

@Entity('users')//typeorm
@ObjectType()//graphql
export class User extends BaseEntity{
    @Field(() => ID)//graphql
    @PrimaryGeneratedColumn()//typeorm
    id: number;

    @Field(() => String)
    @Column()
    firstName: string;
    
    @Field(() => String)
    @Column()
    lastName: string;

    @Field(() => Number)
    @Column()
    age: number;

}
