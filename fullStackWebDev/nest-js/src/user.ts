import { Hobby } from './hobby';
import { ObjectType, Field, Int } from '@nestjs/graphql';

@ObjectType()
export class User {
  @Field(type => Int)
  id: number;

  @Field(type => Date, { name: 'registeredAt' })
  createdAt: Date;

  @Field(type => Date)
  updatedAt: Date;

  @Field(type => String)
  email: string;

  password: string;

  @Field(type => String, { nullable: true })
  name?: string;

  @Field(type => [Hobby])
  hobbies: Hobby[];
}
