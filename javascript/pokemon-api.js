import * as fs from 'node:fs';
let baseUrl = "https://pokeapi.co/api/v2/";
//let pokemonName = "ekans"
let endpoints = await getUrl(baseUrl);
let pokemon = [];
for (const endpoint in endpoints) {
    if (endpoint == "pokemon"){
        let next = `${baseUrl}${endpoint}`;
        while (next){
            let page = await getUrl(next);
            next = page.next;
            pokemon = pokemon.concat(page.results);
        }
        break;
    };
};
for (const [index, mon] of pokemon.entries()) {
    let monDetails = await getUrl(mon.url);
    pokemon[index].heightFt = (monDetails.height/10*3.28084).toFixed(2);
    pokemon[index].weightLbs = ((monDetails.weight/10)*2.2).toFixed(2);
}
console.log(await getUrl(pokemon[0].url));
fs.writeFileSync("pokemon-info.json", JSON.stringify(pokemon, null, 4));
//logObject(await getUrl(`${baseUrl}${endpoint}`));

async function getUrl(url){
    console.log(url);
    let returnData = {};
    // Make a GET request
    await fetch(url)
    .then(response => {
        if (!response.ok) {
            throw new Error('Network response was not ok');
        };
        return response.json();
        })
    .then(data => {
        returnData = data;
    })
    .catch(error => {
        console.error('There was a problem fetching the data:', error);
    });
    return returnData;
}

function logObject(obj){
    for (const key of Object.keys(obj)){
        console.log(`The ${key} is ${obj[key]}`);
    };
}