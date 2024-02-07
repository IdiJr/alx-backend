import redis from 'redis';

// Create a new Redis client
const publisher = redis.createClient();

// Event listener for successful connection
publisher.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for connection error
publisher.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Function to publish a message to the 'holberton school' channel after a certain time
function publishMessage(message, time) {
  setTimeout(() => {
    console.log(`About to send ${message}`);
    publisher.publish('holberton school', message);
  }, time);
}

// Call the publishMessage function with different messages and times
publishMessage('Holberton Student #1 starts course', 100);
publishMessage('Holberton Student #2 starts course', 200);
publishMessage('KILL_SERVER', 300);
publishMessage('Holberton Student #3 starts course', 400);
