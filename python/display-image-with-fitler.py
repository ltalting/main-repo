import pygame

# Initialize pygame
pygame.init()

screenWidth = 100
screenHeight = 100
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Pokemon Viewer")

# Load image
image = pygame.image.load("./python/p6e09fd8.png").convert_alpha()

# Create a red filter (same size as image)
red_filter = pygame.Surface(image.get_size(), pygame.SRCALPHA)
red_filter.fill((255, 0, 0, 100))  # Red with alpha = 100 for transparency

# Apply the filter
image.blit(red_filter, (0, 0), special_flags=pygame.BLEND_RGBA_MULT)

# Display it in a window
screen = pygame.display.set_mode(image.get_size())
screen.blit(image, (0, 0))
pygame.display.flip()

# Wait before quitting
pygame.time.wait(3000)
pygame.quit()