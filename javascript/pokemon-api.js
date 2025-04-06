import * as fs from 'node:fs';
import getUrl from './https/url-functions.js';
import logger from './common/log.js';

let writeLog = true;
let baseUrl = "https://pokeapi.co/api/v2/";
let pokemonName = "";
let endpoints = await getUrl(baseUrl, null, writeLog);
let pokemonRaw = [];
let pokemon = []

// Gather raw pokemon data
for (const endpoint in endpoints) {
    if (endpoint == "pokemon"){
        if (pokemonName.length > 0){
            let page = await getUrl(`${next}/${pokemonName}`, null, writeLog);
            if (JSON.stringify(page) == "{}" || [null,undefined].includes(page)) {
                throw new Error(`Pokemon name '${pokemonName}' was not found.`);
            };
            let pokeIndex = page.species.url.split('/').slice(-2)[0];
            page = await getUrl(`${next}/${pokeIndex}`, null, writeLog);
            pokemonRaw = pokemonRaw.concat(page);
        } else {
            let index = 0;
            let pageSize = 500;
            let queryParameters = {
                "offset": index,
                "limit": pageSize
            };
            let next = `${baseUrl}${endpoint}`;
            while (next) {
                let page = await getUrl(next, queryParameters, writeLog);
                pokemonRaw = pokemonRaw.concat(page.results);
                // Take a step
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
        "name": "",
        "heightFt": null,
        "weightLbs": null
    }
    let monDetails = mon;
    if (mon.url){
        monDetails = await getUrl(mon.url, null, writeLog);
    }
    monObj.name = monDetails.name.replace(/^./, function (match) {
        return match.toUpperCase();
    });
    monObj.heightFt = parseFloat((monDetails.height/10*3.28084).toFixed(2));
    monObj.weightLbs = parseFloat(((monDetails.weight/10)*2.2).toFixed(2));
    pokemon.push(monObj);
};
fs.writeFileSync("pokemon-info.json", JSON.stringify(pokemon, null, 4));