import pygame
import pygameTools
import pokeApi
import pythonHelpers
import getUrl
from io import BytesIO

pygame.init()

def main():
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
        clock.tick(60)

def parsePokemon(pokemon):
     pokemonInfo = {}
     pokemonInfo["name"] = pokemon["name"]
     pokemonInfo["type1"] = pokemon["types"][0]["type"]["name"]
     #pokemonInfo["type2"] = pokemon["types"][1]["type"]["name"]
     pokemonInfo["spriteUrl"] = pokemon["sprites"]["front_default"]
     return pokemonInfo

# W:1024:800
# H:768:600
# Create Screen
screenWidth = 1024
screenHeight = 768
screenLRPad = (20/1024) * screenWidth
screenTBPad = (20/1024) * screenHeight
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pokemon Viewer")

# Add buttons
buttonHeight = (50/1024) * screenHeight
buttonWidth = (200/1024) * screenWidth
buttonBack = pygame.Rect(screenLRPad, (screenHeight - (screenTBPad + buttonHeight)), buttonWidth, buttonHeight)
buttonNext = pygame.Rect((screenWidth - (screenLRPad + buttonWidth)), (screenHeight - (screenTBPad + buttonHeight)), buttonWidth, buttonHeight)
pygameTools.drawButton(screen, buttonBack, "Back")
pygameTools.drawButton(screen, buttonNext, "Next")

# Define where the Pokemon cards will be drawn and how they will be scaled
cardWidth = (540/1024) * screenWidth
cardHeight = (960/1024) * screenHeight
cardX = (screenWidth - cardWidth) // 2
cardY = (screenHeight - cardHeight) // 2

# Get First Pokemon Details
firstPokemon = pokeApi.get_pokemon_by_id_name("9")
firstPokemon = parsePokemon(firstPokemon)
print(firstPokemon)

# Get First Card Image
firstImage = pygame.image.load(BytesIO(pokeApi.get_pokemon_card_image(firstPokemon["type1"]))).convert_alpha()
firstImage = pygame.transform.smoothscale(firstImage,(cardWidth, cardHeight))
screen.blit(firstImage, (cardX, cardY))

# Get First Pokemon Sprite
spriteWidth = (250/1024) * screenWidth
spriteHeight = (250/1024) * screenHeight
spriteX = (screenWidth - spriteWidth) // 2
spriteY = (screenHeight - spriteHeight) // 2 - 150
firstPokemonSprite = pygame.image.load(BytesIO(getUrl.get_url_content(firstPokemon["spriteUrl"]))).convert_alpha()
firstPokemonSprite = pygame.transform.smoothscale(firstPokemonSprite,(spriteWidth, spriteHeight))
screen.blit(firstPokemonSprite, (spriteX, spriteY))

pygame.display.flip()
main()