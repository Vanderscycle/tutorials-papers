import { NestFactory } from '@nestjs/core';
import {
  FastifyAdapter,
  NestFastifyApplication,
} from '@nestjs/platform-fastify'; //first package to install
import fastify from 'fastify';
import { AppModule } from './app.module';

async function bootstrap() {
  const server = fastify({logger: true})

  server.register(require('fastify-cors'), { 
      origin: true,
      methods: ["GET","POST", "DELETE", "PUT", "PATCH"]
    })

  const app = await NestFactory.create<NestFastifyApplication>(
    AppModule,
    new FastifyAdapter(server)
  );
  // app.enableCors();
  
  await app.listen(process.env.SERVER_PORT ?? 3000, '0.0.0.0', (err, address)=>{
    if(err){
        console.log(err)
        process.exit(1)
    }
    console.log(`Server listening on ${address}`)
});//it only works in 127/0/0/1 ask the boss on how to make it localhost
}
bootstrap();

