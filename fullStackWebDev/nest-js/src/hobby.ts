import { ObjectType, Field, Int } from '@nestjs/graphql';


@ObjectType()
export class Hobby {
  @Field(type => Int)
  id: number;

  @Field(type => String)
  name: string;
}
