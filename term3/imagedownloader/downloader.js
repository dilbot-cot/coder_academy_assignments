// Synchronous library for file IO
const fs = require("node:fs");

// Asynchronous function, making directory can take time
const {mkdir} = require("node:fs/promises");

// Streaming data, safer than traditional downloading
// Synchronous
const {Readable} = require("node:stream");

// Wait for streaming to finish, can take time.
const {finished} = require("node:stream/promises");

// Node file & directory path helper 
// ./folder/subfolder/filename.extension
const path = require("node:path")

const API_BASE_URL = "https://pokeapi.co/api/v2/pokemon/";

function downloadPokemonPicture(targetId = getRandomPokemonId()){

}

// return random number 1-1017
function getRandomPokemonId() {
    return Math.floor(Math.random() * 1017)+1
}

// Get Pokemon data for the id
// Get image url from that data
async function getPokemonPictureUrl(targetId = getRandomPokemonId()){

}

// Download the image and save to computer
// Return the image file path
async function savePokemonPictureToDisk(targetUrl, targetDownloadFilename, targetDownloadDirectory = "./images"){

}

module.exports = {
    downloadPokemonPicture,
    getRandomPokemonId,
    getPokemonPictureUrl,
    savePokemonPictureToDisk
}