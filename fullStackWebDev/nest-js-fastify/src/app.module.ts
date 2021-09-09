import { Module } from '@nestjs/common';
import { GraphQLModule } from '@nestjs/graphql';
import { join } from 'path';
import { CatsResolver } from './cats/cats.resolver';

@Module({
  imports: [
    CatsResolver,
    GraphQLModule.forRoot({
      autoSchemaFile: join('schema.gql'),
      debug: true,
      playground: true
    })
  ]
})
export class AppModule {}
