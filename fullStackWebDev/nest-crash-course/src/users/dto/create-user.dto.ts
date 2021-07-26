import { ApiProperty } from "@nestjs/swagger";

//data transfer object
export class CreateUserDto {
  @ApiProperty() //required for any post propreties
  name: string;

  @ApiProperty({required: false})
  age?: number;
  }
  
