import { NestFactory } from '@nestjs/core';
import {
  FastifyAdapter,
  NestFastifyApplication,
} from '@nestjs/platform-fastify';
import fastify from 'fastify';
import { AppModule } from './app.module';

async function bootstrap() {
  const server = fastify()
  server.register(require('fastify-cors'), { //or app.enableCors()
    // put your options here
  })
  server.get('/', (request, reply) => {
  reply.send({ hello: 'world' })
})

  const app = await NestFactory.create<NestFastifyApplication>(
    AppModule,
    new FastifyAdapter(server)
  );
  // app.enableCors();
  
  await app.listen(3000);
}
bootstrap();
