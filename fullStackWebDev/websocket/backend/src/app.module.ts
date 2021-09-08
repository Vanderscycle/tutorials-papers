import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { MsgGatewatModule } from './msgWebsocket/msg.module';

@Module({
  imports: [MsgGatewatModule],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule { }
