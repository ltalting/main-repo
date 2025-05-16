import requests
import json

baseUrl = "https://pokeapi.co/api/v2"

def get_pokemon_card_image(types=None,quality=None):
    ALLOWED_TYPES = [
        "grass",
        "fire",
        "water",
        "lightning",
        "psychic",
        "fighting",
        "dark",
        "metal",
        "dragon",
        "colorless"
    ]

    MAPPED_TYPES = {
        "bug": "grass",
        "normal": "colorless",
        "poison": "dark",
        "electric": "lightning",
        "ground": "fighting",
        "fairy": "psychic",
        "rock": "fighting",
        "ghost": "psychic",
        "ice": "water",
        "steel": "metal"
    }

    if not types:
        types = ALLOWED_TYPES
    else:
        types = types.split(",")
        types = [t.lower() for t in types]
    
    if not quality:
        quality = 100
    
    for type in types:
        if type in ALLOWED_TYPES:
            url = f"https://pokecardmaker.net/_next/image?url=/assets/cards/baseSets/scarletAndViolet/supertypes/pokemon/types/{type}/subtypes/basic.png&w=1280&q={quality}"
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
                return response.content
            except requests.exceptions.RequestException as e:
                print(f"Error fetching {url}: {e}")
                return None
        elif type in MAPPED_TYPES:
            type = MAPPED_TYPES.get(type)
            url = f"https://pokecardmaker.net/_next/image?url=/assets/cards/baseSets/scarletAndViolet/supertypes/pokemon/types/{type}/subtypes/basic.png&w=1280&q={quality}"
            try:
                response = requests.get(url)
                response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
                return response.content
            except requests.exceptions.RequestException as e:
                print(f"Error fetching {url}: {e}")
                return None
        else:
            raise ValueError(f"{type} is not a valid type.")

def get_pokemon_by_id_name(name):
    url = f"{baseUrl}/pokemon/{name}"
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        print(f"Error fetching {url}: {e}")
        return None