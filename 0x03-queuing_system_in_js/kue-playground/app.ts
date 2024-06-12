import { Response, Request } from "express";

const express = require("express");
const kue = require("kue");
const app = express();
const port = 3000;
const axios = require("axios");
const queue = kue.createQueue();
app.get("/", (req: Request, res: Response) => {
  for (let i = 1; i <= 20; i++) {
    queue
      .create("queue example", {
        title: "This testing request",
        data: i,
      })
      .priority("high")
      .save();
  }
  res.send("Hello World!");
  queue.process("queue example", (job: any, done: any) => {
    axios
      .get("https://jsonplaceholder.typicode.com/todos/" + job.data.data)
      .then((result: any) => {
        console.log(result.data);
        done();
        return result.data;
      })
      .catch((error: any) => done(error));
  });
});
app.use("/kue-api/", kue.app);

app.listen(port, () => console.log(`Example app listening on port ${port}!`));
