import redis from 'redis';

// Create a new Redis client
const subscriber = redis.createClient();

// Event listener for successful connection
subscriber.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for connection error
subscriber.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Subscribe to the 'holberton school' channel
subscriber.subscribe('holberton school');

// Event listener for messages received on the subscribed channel
subscriber.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILL_SERVER') {
    subscriber.unsubscribe();
    subscriber.quit();
  }
});
