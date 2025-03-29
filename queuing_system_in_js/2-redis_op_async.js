const client = redis.createClient();
const getAsync = promisify(client.get).bind(client);

client.on('connect', () => {
    console.log('Redis client connected to the server');
});

client.on('error', (error) => {
    console.error(`Redis client not connected to the server: ${error}`);
});

async function setNewSchool(schoolName, value) {
    return new Promise((resolve, reject) => {
        client.set(schoolName, value, (err, reply) => {
            if (err) reject(err);
            else resolve(reply);
        });
    });
}

async function displaySchoolValue(schoolName) {
    try {
        const foundValue = await getAsync(schoolName);
        console.log(foundValue);
    } catch (error) {
        console.error(`Error retrieving value for ${schoolName}: ${error}`);
    }
}

(async function main() {
    await displaySchoolValue('Holberton');
    await setNewSchool('HolbertonSanFrancisco', '100');
    await displaySchoolValue('HolbertonSanFrancisco');
})();