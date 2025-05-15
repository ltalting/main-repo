import pygame
import sys

def get_evenly_distributed_rects(screen_width, screen_height, rect_width, rect_height, num_rects):
    total_rect_width = num_rects * rect_width
    gap = (screen_width - total_rect_width) / (num_rects + 1)

    rects = []
    y = (screen_height - rect_height) // 2  # Center vertically
    for i in range(num_rects):
        x = gap + i * (rect_width + gap)
        rects.append((int(x), int(y)))
    return rects

# --- Main visualization using pygame ---
def main():
    pygame.init()
    
    # Settings
    screen_width, screen_height = 800, 600
    rect_width, rect_height = 50, 100
    num_rects = 1

    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Evenly Distributed Rectangles")

    positions = get_evenly_distributed_rects(screen_width, screen_height, rect_width, rect_height, num_rects)

    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill((240, 240, 240))

        # Draw the rectangles
        for pos in positions:
            pygame.draw.rect(screen, (0, 100, 200), pygame.Rect(pos[0], pos[1], rect_width, rect_height))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()