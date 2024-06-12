import redis from "redis";
import util from "util";

const client = redis.createClient();
const redisGet = util.promisify(client.get);

client
  .on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  })
  .on("connect", () => {
    console.log("Redis client connected to the server");
  });

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  await redisGet(schoolName, (err, value) => {
    if (err) throw err;
    console.log(value);
  });
}

displaySchoolValue("Holberton");
setNewSchool("HolbertonSanFrancisco", "100");
displaySchoolValue("HolbertonSanFrancisco");
