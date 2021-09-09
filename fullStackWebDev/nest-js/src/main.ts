 
import { NestFactory } from "@nestjs/core";
import fastify from "fastify";
import { FastifyAdapter, NestFastifyApplication } from "@nestjs/platform-fastify";
import { AppModule } from "./app.module";

async function bootstrap() {
  const server = fastify();

  const app = await NestFactory.create<NestFastifyApplication>(AppModule, {
    cors: true,
    ...new FastifyAdapter(server),
  });

  app.enableCors();
  await app.listen(process.env.SERVER_PORT, "0.0.0.0");
}
bootstrap();
