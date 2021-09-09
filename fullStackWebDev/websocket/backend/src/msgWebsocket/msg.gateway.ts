import { Logger } from '@nestjs/common';
import { SubscribeMessage, WebSocketGateway, OnGatewayInit, WebSocketServer, WsResponse, OnGatewayConnection, OnGatewayDisconnect } from '@nestjs/websockets';
import { Socket, Server } from 'socket.io';

@WebSocketGateway({ namespace: '/chat' })
export class MsgGateway implements OnGatewayInit, OnGatewayConnection, OnGatewayDisconnect {
  @WebSocketServer() server
  private logger: Logger = new Logger('MsgGateway')

  afterInit(server: Server) {
    this.logger.log("bloody websocket init")
  }

  handleConnection(client: Socket, ...args: any[]) {
    //ids are unique and different each time a user connects
    this.logger.log(`Client connected ${client.id}`)
  }

  handleDisconnect(client: Socket) {
    this.logger.log(`Client disconnected ${client.id}`)
  }

  @SubscribeMessage('msgToServer')
  handleMessage(client: Socket, payload: string): void { //: WsResponse<string> {
    // not type safe
    //this.server.emit('msgToClient', payload)
    this.logger.log(`The client sent the following message to the server ${payload}`)
    client.emit('msgToClient', payload)
    //return { event: 'msgToClient', data: payload };
  }
}
