#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error) {
    const TODO = JSON.parse(body);
    let taskComplete = {};
    TODO.forEach((todo) => {
      if (todo.taskComplete && taskComplete[todo.userId] === undefined) {
        taskComplete[todo.userId] = 1;
      } else if (todo.taskComplete) {
        taskComplete[todo.userId] += 1;
      }
    });
    console.log(taskComplete);
  }
});
