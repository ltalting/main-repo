import pygame
import pygameTools
import pokeApi
import pythonHelpers
import getUrl
from io import BytesIO

pygame.init()

def main():
    index = 1000
    getPokemonByIdNameOutput = pokeApi.get_pokemon_by_id_name(index)
    card, sprite = getCardImages(cardWidth, cardHeight, spriteWidth, spriteHeight, getPokemonByIdNameOutput)
    clock = pygame.time.Clock()
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if buttonBack.collidepoint(event.pos):
                    print("Back button clicked!")
                    index -= 1
                    if index <= 0:
                        index = 1
                    card, sprite = getCardImages(cardWidth, cardHeight, spriteWidth, spriteHeight, index)
                elif buttonNext.collidepoint(event.pos):
                    print("Next button clicked!")
                    index += 1
                    card, sprite = getCardImages(cardWidth, cardHeight, spriteWidth, spriteHeight, index)

        # Clear screen
        screen.fill((0, 0, 0))

        # Draw everything every frame

        # Apply the filter
        backdrop = pygame.image.load("./python/p6e09fd8.png").convert_alpha()
        backdrop = pygame.transform.smoothscale(backdrop,(cardSpriteBoxWidth, cardSpriteBoxHeight))
        red_filter = pygame.Surface(backdrop.get_size(), pygame.SRCALPHA)
        red_filter.fill((255, 0, 0, 100))
        backdrop.blit(red_filter, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)
        screen.blit(card, (cardX, cardY))
        screen.blit(backdrop, (cardSpriteBoxX, cardSpriteBoxY))
        screen.blit(sprite, (spriteX, spriteY))
        pygameTools.drawButton(screen, buttonBack, "Back")
        pygameTools.drawButton(screen, buttonNext, "Next")

        pygame.display.flip()
        clock.tick(60)

def parsePokemon(pokemon):
     pokemonInfo = {}
     pokemonInfo["name"] = pokemon.get("name", "")
     pokemonInfo["type1"] = pokemon.get("types", [])[0].get("type", {}).get("name", "")
     if len(pokemon.get("types", [])) > 1:
        pokemonInfo["type2"] = pokemon.get("types", [])[1].get("type", {}).get("name", "")
     else:
        pokemonInfo["type2"] = ""
     pokemonInfo["spriteUrl"] = pokemon["sprites"]["front_default"]
     return pokemonInfo

def getCardImages(cardWidth, cardHeight, spriteWidth, spriteHeight, getPokemonByIdNameOutput):
    # Get Pokemon Details
    if isinstance(getPokemonByIdNameOutput, str) or isinstance(getPokemonByIdNameOutput, int):
        print(getPokemonByIdNameOutput)
        pokemon = pokeApi.get_pokemon_by_id_name(getPokemonByIdNameOutput)
        pokemon = parsePokemon(pokemon)
    elif "types" in getPokemonByIdNameOutput:
        pokemon = parsePokemon(getPokemonByIdNameOutput)
    else:
        pokemon = pokeApi.get_pokemon_by_id_name(1)
        pokemon = parsePokemon(pokemon)

    # Get Card Image
    cardImage = pygame.image.load(BytesIO(pokeApi.get_pokemon_card_image(pokemon["type1"]))).convert_alpha()
    cardImage = pygame.transform.smoothscale(cardImage,(cardWidth, cardHeight))

    # Get Pokemon Sprite
    spriteImage = pygame.image.load(BytesIO(getUrl.get_url_content(pokemon["spriteUrl"]))).convert_alpha()
    spriteImage = pygame.transform.smoothscale(spriteImage,(spriteWidth, spriteHeight))
    return (cardImage, spriteImage)

# W:1024:800
# H:768:600
# Create Screen
screenWidth = 800
screenHeight = 600
screenLRPad = (20/1024) * screenWidth
screenTBPad = (20/1024) * screenHeight
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pokemon Viewer")

# Add buttons
buttonHeight = (50/1024) * screenHeight
buttonWidth = (200/1024) * screenWidth
buttonBack = pygame.Rect(screenLRPad, (screenHeight - (screenTBPad + buttonHeight)), buttonWidth, buttonHeight)
buttonNext = pygame.Rect((screenWidth - (screenLRPad + buttonWidth)), (screenHeight - (screenTBPad + buttonHeight)), buttonWidth, buttonHeight)

# Define where the Pokemon cards will be drawn and how they will be scaled
cardWidth = (540/1024) * screenWidth
cardHeight = (960/1024) * screenHeight
cardX = (screenWidth - cardWidth) // 2
cardY = (screenHeight - cardHeight) // 2

# Define where the sprites will be drawn and how they will be scaled
spriteWidth = (250/1024) * screenWidth
spriteHeight = (250/1024) * screenHeight
spriteX = (screenWidth - spriteWidth) // 2
spriteY = (screenHeight - spriteHeight) // 2 - ((200/1024) * screenHeight)

# Define the card's sprite area (the area a Pokemon card's artwork normally is)
cardSpriteBoxWidth = (870/1024) * cardWidth
cardSpriteBoxHeight = (388/1024) * cardHeight
cardSpriteBoxX = ((3/540) * cardWidth) + cardX + (cardWidth - cardSpriteBoxWidth) / 2
cardSpriteBoxY = cardY + (cardHeight / 2) - ((412/1024) * cardHeight)

main()