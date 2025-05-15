import pygame

def getRectScreenCenterCoord(screenWidth,screenHeight,rectWidth,rectHeight):
    x = (screenWidth - rectWidth) // 2
    y = (screenHeight - rectHeight) // 2
    return (x, y, rectWidth, rectHeight)

def getEvenlyDistributedRectsHoriz(screen_width, screen_height, rect_width, rect_height, num_rects):
    total_rect_width = num_rects * rect_width
    gap = (screen_width - total_rect_width) / (num_rects + 1)

    rects = []
    y = (screen_height - rect_height) // 2  # Center vertically
    for i in range(num_rects):
        x = gap + i * (rect_width + gap)
        rects.append((int(x), int(y)))
    return rects

def getEvenlyDistributedRectsVert(screen_width, screen_height, rect_width, rect_height, num_rects):
    total_rect_height = num_rects * rect_height
    gap = (screen_height - total_rect_height) / (num_rects + 1)

    rects = []
    x = (screen_width - rect_width) // 2  # Center horizontally
    for i in range(num_rects):
        y = gap + i * (rect_height + gap)
        rects.append((int(x), int(y)))
    return rects

def drawButton(screen,button,text,fontName="Arial",fontSize=25):
    font = pygame.font.SysFont(fontName, fontSize)
    # Draw the button (change color if hovered)
    mouse_pos = pygame.mouse.get_pos()
    if button.collidepoint(mouse_pos):
        pygame.draw.rect(screen, (0, 255, 255), button)  # Hover effect
    else:
        pygame.draw.rect(screen, (0, 128, 255), button)
    text = font.render(text, True, (255, 255, 255))
    text_rect = text.get_rect(center = button.center)
    screen.blit(text, text_rect)