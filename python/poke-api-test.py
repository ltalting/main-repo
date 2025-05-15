import pokeApi
import json
# Get Pokemon Details
firstPokemon = pokeApi.get_pokemon_by_name("bulbasaur")
print(json.loads(firstPokemon))