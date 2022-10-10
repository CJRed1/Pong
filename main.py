# Import Pygame
import pygame

# Initialize Pygame
pygame.init()

# Colors
color_background = (100, 100, 100)
color_player1 = (255, 0, 0)
color_player2 = (0, 0, 255)
color_ball = (255, 255, 0)
color_line = (255, 255, 255)

# Sizes
player_width = 15
player_height = 60
ball_radius = 10

# Coords
player1_x = 50
player1_y = 300
player2_x = 725
player2_y = 300
ball_x = 400
ball_y = 325

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

    # Drawing area

    # Define the Players
    player_1 = pygame.draw.rect(screen, color_player1, (player1_x, player1_y, player_width, player_height))
    player_2 = pygame.draw.rect(screen, color_player2, (player2_x, player2_y, player_width, player_height))
    
    # Draw the Line
    line = pygame.draw.aaline(screen, color_line, (screen_width/2, 2), (screen_width/2, screen_height-4))

    # Draw the Ball
    ball = pygame.draw.circle(screen, color_ball, (ball_x, ball_y), ball_radius)

    # Refresh the window
    pygame.display.flip()