

## Description

[Nest](https://github.com/nestjs/nest) framework TypeScript starter repository.

## Installation

```bash
$ npm install
```

## Running the app

```bash
# development
$ npm run start

# watch mode
$ npm run start:dev

# production mode
$ npm run start:prod
```

## Test

```bash
# unit tests
$ npm run test

# e2e tests
$ npm run test:e2e

# test coverage
$ npm run test:cov
```

## Support

Nest is an MIT-licensed open source project. It can grow thanks to the sponsors and support by the amazing backers. If you'd like to join them, please [read more here](https://docs.nestjs.com/support).

## Stay in touch

- Author - [Kamil Myśliwiec](https://kamilmysliwiec.com)
- Website - [https://nestjs.com](https://nestjs.com/)
- Twitter - [@nestframework](https://twitter.com/nestframework)

## License

Nest is [MIT licensed](LICENSE).

## lessons learned

Quick refresher on docker

start command (assuming you have the image)

sudo docker run -it -v mongodata:/data/db --name mongodb -d mongo 
-v (volume) with local data being stored in mongodata 
if you want to bind a port add -p {local port}:{container port} (you can bind an ip:port address to a container port as well)

### NestJs

Enabling fastify
[quick start guide](https://docs.nestjs.com/techniques/performance#performance-fastify)
```
npm i --save @nestjs/platform-fastify
```
Since fastify is now the HTTP provider its important to use [fastify](https://www.fastify.io/docs/latest/) equivalent packages. 
