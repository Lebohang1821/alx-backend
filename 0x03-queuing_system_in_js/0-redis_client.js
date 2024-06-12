#!/usr/bin/yarn dev
import { createClient } from 'redis';

// It import 'createClient' function from 'redis' library.
const client = createClient();

client.on('error', (err) => {
  console.log('Redis client not connected to the server:', err.toString());
});

client.on('connect', () => {
  console.log('Redis client connected to the server');
});
