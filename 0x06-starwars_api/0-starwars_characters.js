#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, async (err, res, body) => {
  err && console.log(err);

  const charactersArr = (JSON.parse(res.body).characters);
  for (const charac of charactersArr) {
    await new Promise((resolve, reject) => {
      request(charac, (err, res, body) => {
        err && console.log(err);

        console.log(JSON.parse(body).name);
        resolve();
      });
    });
  }
});
