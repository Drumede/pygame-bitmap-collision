import pygame
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("bitmap collision")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
DARK_GREEN = (0,140,0)

# Game loop variables
running = True
clock = pygame.time.Clock()
FPS = 60

# Game objects (example: a simple player rectangle)
player_x = SCREEN_WIDTH // 2
player_y = SCREEN_HEIGHT // 2
player_width = 50
player_height = 50
player_color = RED

image_path = "level.png"  # Replace with your image file
image_surface = pygame.image.load(image_path) # Use convert_alpha() for images

pixel_res = 4
colors = []
img_width = image_surface.get_width()
img_height = image_surface.get_height()
grid_width = int(img_width / pixel_res)
grid_height = int(img_height / pixel_res)

for x in range(grid_width):
    colors.append([])
    print(x)
    print(colors)
    for y in range(grid_height):
        print(y*pixel_res)
        colors[x].append(image_surface.get_at((x*pixel_res,y*pixel_res)))
        if colors[x][y] == BLACK:
            colors[x][y] = 1
        else:
            colors[x][y] = 0

print(colors)
# Game loop
while running:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        # Add more event handling here (e.g., keyboard input, mouse clicks)

    # Game logic (update game state)
    # Example: move player based on input, update object positions, check collisions

    # Drawing
    screen.fill(DARK_GREEN)  # Fill background
    screen.blit(image_surface,(0,0))
    # Draw other game elements here

    for x in range(grid_width):
        for y in range(grid_height):
            px_color = BLACK if colors[x][y] == 1  else WHITE
            pygame.draw.rect(screen, px_color, (x*pixel_res*4, y*pixel_res*4, pixel_res*4, pixel_res*4))  # Draw player

    # Update display
    pygame.display.flip()

    # Control frame rate
    clock.tick(FPS)

# Quit Pygame
pygame.quit()