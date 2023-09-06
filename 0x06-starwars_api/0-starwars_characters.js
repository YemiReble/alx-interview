const { readFileSync } = require('fs');
const starWarsApi = require('./starWarsApi');

const filmId = process.argv[2];

const response = await starWarsApi.getFilmCharacters(filmId);
const characters = response.characters;

const lines = characters.map((character) => character.name);

console.log(lines);
