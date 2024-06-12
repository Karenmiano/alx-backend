export default function createPushNotificationsJobs(jobs, queue) {
  if (!Array.isArray(jobs)) {
    throw new Error("Jobs is not an array");
  }
  for (const j of jobs) {
    const job = queue.create("push_notification_code_3", j).save((err) => {
      if (!err) {
        console.log(`Notication job created: ${job.id}`);
      }
    });

    job
      .on("complete", (result) => {
        console.log(`Notification job ${job.id} completed`);
      })
      .on("failed", (errorMessage) => {
        console.log(`Notification job ${job.id} failed: ${errorMessage}`);
      })
      .on("progress", (progress, data) => {
        console.log(`Notification job ${job.id} ${progress}% complete`);
      });
  }
}
