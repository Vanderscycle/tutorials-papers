import { ApiProperty } from "@nestjs/swagger";

export class User {
  @ApiProperty()
  id:number;

  @ApiProperty()
  name: string

  @ApiProperty()
  age?: number
}
