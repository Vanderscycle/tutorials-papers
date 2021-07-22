import { Module } from '@nestjs/common';
import { GraphQLModule } from '@nestjs/graphql'; //this is the road block to convert the app into fastify
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { CatsModule } from './cats/cats.module' 

@Module({
  imports: [
    CatsModule,
    GraphQLModule.forRoot({
    autoSchemaFile: 'schema.gql'
  })],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule {}
