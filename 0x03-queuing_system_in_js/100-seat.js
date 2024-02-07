import express from 'express';
import redis from 'redis';
import kue from 'kue';
import { promisify } from 'util';

// Create express app
const app = express();
const port = 1245;

// Create Redis client
const redisClient = redis.createClient();

// Promisify Redis functions
const getAsync = promisify(redisClient.get).bind(redisClient);
const setAsync = promisify(redisClient.set).bind(redisClient);

// Initialize available seats and reservation status
let availableSeats = 50;
let reservationEnabled = true;

// Create Kue queue
const queue = kue.createQueue();

// Function to reserve seats
async function reserveSeat(number) {
  await setAsync('available_seats', number);
}

// Function to get current available seats
async function getCurrentAvailableSeats() {
  const seats = await getAsync('available_seats');
  return parseInt(seats) || 0;
}

// Route to get available seats
app.get('/available_seats', async (req, res) => {
  res.json({ numberOfAvailableSeats: await getCurrentAvailableSeats() });
});

// Route to reserve a seat
app.get('/reserve_seat', async (req, res) => {
  if (!reservationEnabled) {
    return res.json({ status: 'Reservation are blocked' });
  }
  
  const job = queue.create('reserve_seat').save(err => {
    if (err) {
      return res.json({ status: 'Reservation failed' });
    }
    res.json({ status: 'Reservation in process' });
  });
  
  job.on('complete', result => {
    console.log(`Seat reservation job ${job.id} completed`);
  });
  
  job.on('failed', err => {
    console.log(`Seat reservation job ${job.id} failed: ${err.message}`);
  });
});

// Route to process the queue
app.get('/process', async (req, res) => {
  res.json({ status: 'Queue processing' });
  
  const currentAvailableSeats = await getCurrentAvailableSeats();
  if (currentAvailableSeats === 0) {
    reservationEnabled = false;
  }
  
  queue.process('reserve_seat', async (job, done) => {
    const newAvailableSeats = currentAvailableSeats - 1;
    if (newAvailableSeats < 0) {
      return done(new Error('Not enough seats available'));
    }
    
    await reserveSeat(newAvailableSeats);
    done();
  });
});

// Start server
app.listen(port, () => {
  console.log(`Server is listening on port ${port}`);
});
