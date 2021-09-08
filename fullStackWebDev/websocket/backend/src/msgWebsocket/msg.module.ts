import { Module } from '@nestjs/common';
import { MsgGateway } from './msg.gateway';

@Module({
  providers: [MsgGateway],
})
export class MsgGatewatModule { }
