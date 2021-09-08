import { Test, TestingModule } from '@nestjs/testing';
import { MsgGateway } from './msg.gateway';

describe('MsgGateway', () => {
  let gateway: MsgGateway;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [MsgGateway],
    }).compile();

    gateway = module.get<MsgGateway>(MsgGateway);
  });

  it('should be defined', () => {
    expect(gateway).toBeDefined();
  });
});
