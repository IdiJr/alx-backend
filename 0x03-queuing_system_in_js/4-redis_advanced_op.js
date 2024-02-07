import redis from 'redis';

// Create a new Redis client
const client = redis.createClient();

// Event listener for successful connection
client.on('connect', () => {
  console.log('Redis client connected to the server');
});

// Event listener for connection error
client.on('error', (error) => {
  console.error(`Redis client not connected to the server: ${error}`);
});

// Function to set hash value in Redis
function createHash() {
  client.hset(
    'HolbertonSchools',
    'Portland', 50,
    'Seattle', 80,
    'New York', 20,
    'Bogota', 20,
    'Cali', 40,
    'Paris', 2,
    (error, reply) => {
      if (error) {
        console.error(error);
      } else {
        console.log(`Reply: ${reply}`);
      }
    }
  );
}

// Function to display hash value from Redis
function displayHash() {
  client.hgetall('HolbertonSchools', (error, result) => {
    if (error) {
      console.error(error);
    } else {
      console.log(result);
    }
  });
}

// Call the functions
createHash();
displayHash();
