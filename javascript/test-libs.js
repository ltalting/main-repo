import * as urlFunctions from './libs/https/url-functions.js';

console.log(await urlFunctions.getUrl("https://www.google.com"));
console.log(await urlFunctions.getUrl("https://pokeapi.co/api/v2//pokemon",{"offset":"0","limit":"100"}));