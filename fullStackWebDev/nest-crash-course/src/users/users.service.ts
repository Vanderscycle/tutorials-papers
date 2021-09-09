import { Injectable } from '@nestjs/common';
import { CreateUserDto } from './dto/create-user.dto';
import { User } from './entities/user.entity';

@Injectable()
export class UsersService {
  private users: User[] = [{id:0,name:'Mario'}]

  findAll():User[]{
    return this.users
  }
  findById(userId: number):User {
    return this.users.find(user => user.id === userId)//if it doesn't find the maatch it returns undefined
  }
  createUser(createUserDto:CreateUserDto): User{//before name:string
    const newUser = {id: Date.now(), ...createUserDto}
    this.users.push(newUser)
    return newUser
  }
}
