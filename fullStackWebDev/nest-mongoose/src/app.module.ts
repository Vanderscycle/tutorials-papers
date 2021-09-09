import { Module } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';

import { AppController } from './app.controller';
import { AppService } from './app.service';
import { ProductsModule } from './products/products.module';

@Module({
  imports: [
    ProductsModule,
    // MongooseModule.forRoot('mongodb://mongodb:27018/', {useNewUrlParser: true}),
    MongooseModule.forRoot('mongodb://127.0.0.1:27018/testMongoose', {useNewUrlParser: true}),//TODO: we created db 27018 instead of //HACK: not sure why this works on 127.0.0.1:/port isntead of name container
  ], //:WARN: haven't connected succesfull once
  
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}

//inspect mongo contaienr
//docker exec -it mongodb sh
//docker run --name mongodb -d -v ./mongodb:/data/db -p 27018:27017 mongo:latest

//in mongo cli
//https://www.mongodb.com/basics/create-database/
//use mongo {nameOf instance} 
//show collections
//db.collection_name.find().pretty()


//to connect with mongodb-compass 
//mongodb://127.0.0.1:27018/testMongoose?readPreference=primary&appname=MongoDB%20Compass&directConnection=true&ssl=false
