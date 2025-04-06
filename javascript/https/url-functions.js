import { URLSearchParams } from 'node:url'
export default async function getUrl(url, queryParameters, logging){
    let returnData = {};
    if (queryParameters == null){
        if (logging){
            console.log(`Fetching ${url}...`);
        };
        // Make a GET request
        await fetch(url)
        .then(response => {
            if (!response.ok) {
                throw new Error("Failed to get URL");
            };
            return response.json();
            })
        .then(data => {
            returnData = data;
        })
        .catch(error => {
            console.error('There was a problem fetching the data:', error);
        });
    } else {
        if (typeof queryParameters == "object"){
            returnData = await getUrlWithQueryParameters(url, queryParameters, logging)
        } else {
            throw new Error("queryParameters must be an object.");
        };
    };
    return returnData;
}

async function getUrlWithQueryParameters(url, queryParameters, logging){
    let returnData = {};
    let formedUrl = new URL(url);
    formedUrl.search = new URLSearchParams(queryParameters).toString();
    if (logging){
        console.log(`Fetching ${formedUrl}...`);
    };
    // Make a GET request
    await fetch(formedUrl)
    .then(response => {
        if (!response.ok) {
            throw new Error("Failed to get URL");
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