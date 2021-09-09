import { Body, Controller, Get, Param, Post } from '@nestjs/common';
import { ApiCreatedResponse, ApiOkResponse, ApiTags } from '@nestjs/swagger';
import { CreateUserDto } from './dto/create-user.dto';
import { User } from './entities/user.entity';
import { UsersService } from './users.service';

@ApiTags('users')//header tag for swagger
@Controller('users')
export class UsersController {
  constructor(private userService: UsersService) {} //nestjs uses dependencies injection (nest will automatically instanciates the class)
  @ApiOkResponse({type: User, isArray: true})
  @Get() //required to be a route endpoint handler also if ('') empty that mean its using /users
  getUsers(): User[] {
    return this.userService.findAll()
    // return [{id:0}]//replacing with them using the service layer
  }

  @ApiOkResponse({type: User})
  @Get(':id')
  getUSerById(@Param('id') id:string ): User { //TODO:auto parse
    return this.userService.findById(Number(id))
    // return{ id }
  }
  //swagger docs schema:
  //input: CreateUserDto
  //output response: User (need Api propreties)
  @ApiCreatedResponse({type: User})
  @Post()
  createUser(@Body() body:CreateUserDto): User {//nest-mongoose did a different interpretation of that
    return this.userService.createUser(body)
  }
}

//because we want to emply ts we must import the types for input data (dtos or locally defined) and the return object (entitites)

//swagger
//npm i --save @nestjs/swagger fastify-swagger
