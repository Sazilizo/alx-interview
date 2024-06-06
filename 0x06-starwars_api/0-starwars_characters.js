#!/usr/bin/node
const API = 'https://swapi-api.hbtn.io/api';
const req = require("request");

if (process.argv.length > 2) {
  req(`${API}/films/${process.argv[2]}/`, (err, _, body) => {
    if (err) {
      console.log(err);
    }
    const AllCharacters= JSON.parse(body).characters;
    const characterNames = AllCharacters.map(
      url => new Promise((resolve, reject) => {
        req(url, (err, __, charactersBody) => {
          if (err) {
            reject(err);
          }
          resolve(JSON.parse(charactersBody).name);
        });
      }));

    Promise.all(characterNames)
      .then(names => console.log(names.join('\n')))
      .catch(errors => console.log(errors));
  });
}
