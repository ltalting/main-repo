import * as fs from 'node:fs';
import * as urlFunctions from '../libs/https/url-functions.js';
import logger from '../libs/log/log.js';

let writeLog = true;
let baseUrl = "https://pokeapi.co/api/v2/";
let pokemonName = "pikachu"; // no space, comma-separated list
let endpoints = await urlFunctions.getUrl(baseUrl, null, writeLog);
let pokemonRaw = [];
let pokemon = []

// Loop through each available endpoint
for (const endpoint in endpoints) {
    // Pokemon Endpoint
    // https://pokeapi.co/docs/v2#pokemon-section
    if (endpoint == "pokemon"){
        // Set the "next" page.
        // Ex: https://pokeapi.co/api/v2/pokemon
        let next = `${baseUrl}${endpoint}`;
        // Were pokemonNames provided?
        if (pokemonName.length > 0){
            // Split pokemonName variable by ",", remove trailing space
            let pokemonNames = pokemonName.split(",").filter(str => str.trim() != "");
            // Go through each name
            while (pokemonNames[0]) {
                let pokemonName = pokemonNames[0];
                // Look up the pokemon, error if not found
                let page = await urlFunctions.getUrl(`${next}/${pokemonName}`, null, writeLog);
                if (JSON.stringify(page) == "{}" || [null,undefined].includes(page)) {
                    throw new Error(`Pokemon name '${pokemonName}' was not found.`);
                };
                pokemonRaw = pokemonRaw.concat(page);
                pokemonNames.shift();
            };
        // Nothing specific? Gotta Catch 'Em All
        } else {
            // Initialize paging variables
            let index = 0;
            let pageSize = 500;
            let queryParameters = {
                "offset": index,
                "limit": pageSize
            };
            // While there is a "next" page to get
            while (next) {
                // Get the next page
                // Each page from the URL contains a URL for more detailed
                // information on the pokemon
                // https://pokeapi.co/api/v2/pokemon/1/
                let page = await urlFunctions.getUrl(next, queryParameters, writeLog);
                for (const mon of page.results){
                    // Get each pokemon's detailed information
                    pokemonRaw = pokemonRaw.concat(await urlFunctions.getUrl(mon.url, null, writeLog));
                };
                // Make sure there are no pages left
                if (page.next == null || index > page.count){
                    next = false;
                    break;
                };
                index = index + pageSize;
                queryParameters = {
                    "offset": index,
                    "limit": pageSize
                };
            };
        }
        break;
    };
};

// Translate raw data to expected format
for (const mon of pokemonRaw) {
    let monObj = {
        "id": "",
        "name": "",
        "heightFt": null,
        "weightLbs": null
    };
    monObj.name = mon.name.replace(/^./, function (match) {
        return match.toUpperCase();
    });
    monObj.id = mon.id.toString();
    monObj.heightFt = parseFloat((mon.height/10*3.28084).toFixed(2));
    monObj.weightLbs = parseFloat(((mon.weight/10)*2.2).toFixed(2));
    pokemon.push(monObj);
};
fs.writeFileSync("pokemon-info.json", JSON.stringify(pokemon, null, 2));