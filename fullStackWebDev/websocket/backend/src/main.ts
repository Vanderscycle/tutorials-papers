
import { NestFactory } from '@nestjs/core';
import {
  FastifyAdapter,
  NestFastifyApplication,
} from '@nestjs/platform-fastify'; //first package to install
import fastify from 'fastify';
import * as path from 'path';
import { AppModule } from './app.module';

async function bootstrap() {
  const server = fastify({ logger: true })

  server.register(require('fastify-cors'), {
    origin: true,
    methods: ["GET", "POST", "DELETE", "PUT", "PATCH"]
  })
  //really cool if you want nestJs to serve static files like (html/css)
  server.register(require('fastify-static'), {
    root: path.join(__dirname, '..', 'static'),
    prefix: '/static/', // optional: default '/'
  })
  const app = await NestFactory.create<NestFastifyApplication>(
    AppModule,
    new FastifyAdapter(server)
  );
  //app.useStaticAssets(join(__dirname, '..', 'static')) //INFO: only works for express
  // app.enableCors();

  await app.listen(process.env.SERVER_PORT ?? 3100, '0.0.0.0', (err, address) => {
    if (err) {
      console.log(err)
      process.exit(1)
    }
    console.log()
  });//it only works in 127/0/0/1 ask the boss on how to make it localhost
}
bootstrap();
