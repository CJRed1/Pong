# Import Pygame
import pygame

# Initialize Pygame
pygame.init()

# Colors
color_background = (100, 100, 100)
color_players = (255, 255, 255)
color_ball = (255, 255, 0)

# Window Size
screen_width = 800
screen_height = 600

# Size Variable
size = (screen_width, screen_height)

# Display the window
screen = pygame.display.set_mode(size)

# Title
pygame.display.set_caption("Pong Game")

# Icon
icon = pygame.image.load("pong_icon.png")
pygame.display.set_icon(icon)

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Fill the screen with color
    screen.fill(color_background)

    # Refresh the window
    pygame.display.flip()