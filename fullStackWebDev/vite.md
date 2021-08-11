```bash
npm init vite@latest {folder name} -- --template svelte-ts
cd {folder name}
npx svelte-add@latest tailwindcss

# router
npm install --save svelte-navigator

# testing
npm install --save-dev @testing-library/svelte jest@26 svelte-jester
npm install --save-dev @testing-library/jest-dom
npm install --save-dev cypress @testing-library/cypress
# the ts side
npm i jest @types/jest ts-jest typescript -D
npm install --save-dev cypress-svelte-unit-test
```
```add  to/and create .babelrc
{
  "presets": [["@babel/preset-env", {"targets": {"node": "current"}}]]
}
```
``` add to package.json (jest)
  "jest": {
    "transform": {
      "^.+\\.svelte$": [
        "svelte-jester",
        {
          "preprocess": true
        }
      ],
      "^.+\\.ts$": "ts-jest",
      "^.+\\.js$": "babel-jest"
    },
    "moduleFileExtensions": [
      "js",
      "ts",
      "svelte"
    ]
  },
  "setupFilesAfterEnv": [
    "@testing-library/jest-dom/extend-expect"
  ]
```
``` add to tsconfig.json
  "compilerOptions": {
    "types": ["cypress", "@testing-library/cypress"]
  }
```

```
  scripts:
    "cy:run": "cypress run"
    "test": "jest src",
    "test:watch": "npm run test -- --watch",
```
```bash
mkdir src/__tests__
touch src/__tests__/helloWorldComponent.test.js
touch src/helloWorldButton.svelte

# cypress
$(npm bin)/cypress open
mkdir -p cypress/integration/
touch cypress/integration/test.spec.js
cat > cypress/integration/test.spec.js << EOF

describe('Template store app', () => {
  beforeEach(() => {
    cy.visit('/')
  })

  it('starts with "hello"', () => {
    cy.contains('Hello Typescript!')
  })

})
EOF

touch cypress.json
cat > cypress.json << EOF
{
  "componentFolder": "src",
  "testFiles": "**/*.spec.js",
  "pluginsFile":false,
  "baseUrl":"http://localhost:3000"
}
EOF
```
gitignore
```bash
cat > .gitignore <<EOF
/node_modules/
/dist/
/.vscode/
.DS_Store
package-lock.json
cypress/support/
cypress/videos/
EOF

rm -rf .vscode
```
backend
```bash
nest new backend
npm i --save @nestjs/platform-fastify fastify
npm uninstall @nestjs/platform-express express @types/express
```
```
cat > src/main.ts << EOF

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
EOF
```
```
rm -rf ./backend/.git
```
