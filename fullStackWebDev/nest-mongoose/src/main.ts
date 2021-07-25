import { NestFactory } from '@nestjs/core';
import {
  FastifyAdapter,
  NestFastifyApplication,
} from '@nestjs/platform-fastify';
import fastify from 'fastify';
import { AppModule } from './app.module';

async function bootstrap() {
  const server = fastify()
  server.get('/', (request, reply) => {
    reply.send({ hello: 'worlds2' })
  })

  const app = await NestFactory.create<NestFastifyApplication>(
    AppModule,
    new FastifyAdapter(server)
  );
  app.enableCors();
  
  await app.listen(3000);
}
bootstrap();

