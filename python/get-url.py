import requests

def get_url_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        return response.text
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None

# Example usage:
# https://raw.githubusercontent.com/PokeAPI/sprites/master/sprites/pokemon/1.png
url = "https://www.google.com"
content = get_url_content(url)

if content:
    print(content)