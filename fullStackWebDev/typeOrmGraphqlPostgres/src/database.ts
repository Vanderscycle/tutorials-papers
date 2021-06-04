import { createConnection } from 'typeorm';
import { User } from './entity/user';

export const init_db = async() => {
  const connection = await createConnection();
  await connection.dropDatabase();
  await connection.synchronize();

  // User
  const user = new User();
  user.firstName = 'Timsd1231ber'
  user.lastName = 'chasdaad@chad'
  user.age = 56
  await user.save()

  };
