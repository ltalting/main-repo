import pygame
import pygameTools
import pokeApi
from io import BytesIO

pygame.init()

screenWidth = 800
screenHeight = 600
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pokemon!")

rectPositions = pygameTools.getEvenlyDistributedRectsVert(screenWidth, screenHeight, 400, 20, 2)

button = pygame.Rect(pygameTools.getRectScreenCenterCoord(screenWidth,screenHeight, 300, 50))

clock = pygame.time.Clock()
run = True
while run:
    for rectPos in rectPositions:
        
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if button.collidepoint(event.pos):  # Check if the button is clicked
                content = BytesIO(pokeApi.get_pokemon_card_image("colorless"))
                OVERLAY_IMAGE = pygame.image.load(content).convert_alpha()
                SCREEN_BACKGROUND_OVERLAY = pygame.transform.scale(OVERLAY_IMAGE,(screenWidth, screenHeight))
                screen.blit(SCREEN_BACKGROUND_OVERLAY, (0, 0))
    pygameTools.drawButton(screen,button, "Arial", 30)
    pygame.display.flip()
    clock.tick(60)
pygame.quit()