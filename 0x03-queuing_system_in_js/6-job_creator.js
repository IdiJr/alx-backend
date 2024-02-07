import kue from 'kue';

// Create a queue with Kue
const queue = kue.createQueue();

// Object containing the Job data
const jobData = {
  phoneNumber: '4153518780',
  message: 'This is the code to verify your account',
};

// Create a job and add it to the queue
const job = queue.create('push_notification_code', jobData);

// Event listener for job creation
job.on('enqueue', () => {
  console.log(`Notification job created: ${job.id}`);
});

// Event listener for job completion
job.on('complete', () => {
  console.log('Notification job completed');
});

// Event listener for job failure
job.on('failed', () => {
  console.log('Notification job failed');
});

// Save the job to the queue
job.save();
