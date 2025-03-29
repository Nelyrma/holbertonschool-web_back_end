import  { createClient, print } from 'redis';

const client = createClient();

client.on('error', (error) => console.log('Redis client not connected to the server: ' + error.toString()));

client.on('connect', () => console.log('Redis client connected to the server'));

const fieldsValues = {
  Portland: 50,
  Seattle: 80,
  'New York': 20,
  Bogota: 20,
  Cali: 40,
  Paris: 2
};

for (const [field, value] of Object.entries(fieldsValues)) {
  client.hset('HolbertonSchools', field, value, (error, reply) => {
    print('Reply: ' + reply);
  });
}

client.hgetall('HolbertonSchools', (error, result) => {
  console.log(result);
});