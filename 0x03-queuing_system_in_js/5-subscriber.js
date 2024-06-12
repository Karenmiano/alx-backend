import redis from "redis";

const sub = redis.createClient();

sub
  .on("error", (err) => {
    console.log(`Redis client not connected to the server: ${err}`);
  })
  .on("connect", () => {
    console.log("Redis client connected to the server");
  });

sub.subscribe("holberton school channel");
// event-listener for messages
sub.on("message", (channel, message) => {
  if (channel === "holberton school channel") {
    if (message === "KILL_SERVER") {
      sub.unsubscribe();
      sub.quit();
    }
    console.log(message);
  }
});
