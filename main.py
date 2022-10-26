# Import
import pygame
import random as rd

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

# Speeds
player1_vspeed = 0
player2_vspeed = 0
ball_speed = 0.2
ball_hspeed = rd.choice([-ball_speed, ball_speed])
ball_vspeed = rd.choice([-ball_speed, ball_speed])

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

# Sounds
paddle = pygame.mixer.Sound("sounds/paddle.mp3")
wall = pygame.mixer.Sound("sounds/wall.mp3")
score = pygame.mixer.Sound("sounds/score.mp3")
jingle = pygame.mixer.Sound("sounds/jingle.mp3")
pygame.mixer.Sound.set_volume(paddle, 0.2)
pygame.mixer.Sound.set_volume(wall, 0.2)
pygame.mixer.Sound.set_volume(score, 0.2)
pygame.mixer.Sound.set_volume(jingle, 0.2)

back_music = pygame.mixer.music.load("sounds/back_music.mp3")
pygame.mixer.music.set_volume(0.1)
pygame.mixer.music.play(-1)

# Score Variables
player1_score = 0
player2_score = 0

# Score Font
score_font = pygame.font.Font("PixelEmulator-xq08.ttf", 32)
winner_font = pygame.font.Font("PixelEmulator-xq08.ttf", 64)

# Score Position
p1score_x = 10
p2score_x = 410
score_y = 10

# Winner Position
winner_x = 200
winner_y = 200
game_won = 0

# Show Score
def show_score(x, x2, y):
    score1 = score_font.render("P1: " + str(player1_score), True, color_line)
    score2 = score_font.render("P2: " + str(player2_score), True, color_line)
    screen.blit(score1, (x, y))
    screen.blit(score2, (x2, y))

# Show Winner
def show_winner(x, y, winner):
    if winner == 1:
        winner1 = winner_font.render("P1 Wins!!", True, (255, 50, 50))
        screen.blit(winner1, (x, y))
    elif winner == 2:
        winner2 = winner_font.render("P2 Wins!!", True, (50, 50, 255))
        screen.blit(winner2, (x, y))

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        # Players Key Check
        if event.type == pygame.KEYDOWN:

            # Player 1
            if event.key == pygame.K_w:
                player1_vspeed = -0.5

            if event.key == pygame.K_s:
                player1_vspeed = 0.5

            # Player 2
            if event.key == pygame.K_UP:
                player2_vspeed = -0.5

            if event.key == pygame.K_DOWN:
                player2_vspeed = 0.5

        if event.type == pygame.KEYUP:
            
            # Player 1
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player1_vspeed = 0

            # Player 2
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2_vspeed = 0

    if player1_y + player1_vspeed >= 0 and player1_y + player1_vspeed + player_height <= screen_height:
        player1_y += player1_vspeed
    if player2_y + player2_vspeed >= 0 and player2_y + player2_vspeed + player_height <= screen_height:
        player2_y += player2_vspeed

    ball_x += ball_hspeed
    ball_y += ball_vspeed

    if ball_x <= 0:
        pygame.mixer.Sound.play(score)
        ball_hspeed = rd.choice([-ball_speed, ball_speed])
        player2_score += 1
        ball_x = 400
        ball_y = 325

    if ball_x + ball_radius >= screen_width:
        pygame.mixer.Sound.play(score)
        ball_hspeed = rd.choice([-ball_speed, ball_speed])
        player1_score += 1
        ball_x = 400
        ball_y = 325

    if ball_y <= 0 or ball_y + ball_radius >= screen_height:
        pygame.mixer.Sound.play(wall)
        ball_vspeed *= -1

    # Fill the screen with color
    screen.fill(color_background)

    # Drawing area

    # Define the Players
    player_1 = pygame.draw.rect(screen, color_player1, (player1_x, player1_y, player_width, player_height))
    player_2 = pygame.draw.rect(screen, color_player2, (player2_x, player2_y, player_width, player_height))
    
    # Draw the Line
    line = pygame.draw.aaline(screen, color_line, (screen_width/2, 2), (screen_width/2, screen_height-4))
    line_middle = pygame.draw.circle(screen, color_line, (screen_width/2, screen_height/2+30), 90, 1)

    # Draw the Ball
    ball = pygame.draw.circle(screen, color_ball, (ball_x, ball_y), ball_radius)

    # Collisions
    if ball.colliderect(player_1):
        pygame.mixer.Sound.play(paddle)
        ball_hspeed *= -1.01
        ball_x += 1
    if ball.colliderect(player_2):
        pygame.mixer.Sound.play(paddle)
        ball_hspeed *= -1.01
        ball_x -= 1

    # Show Score
    show_score(p1score_x, p2score_x, score_y)

    # Show Winner

    if player1_score >= 10:
        game_won = 1
        player1_score = 0
        player2_score = 0
        pygame.mixer.Sound.play(jingle)
        pygame.mixer.music.pause()
    elif player2_score >= 10:
        game_won = 2
        player1_score = 0
        player2_score = 0
        pygame.mixer.Sound.play(jingle)
        pygame.mixer.music.pause()
    
    if game_won == 1:
        show_winner(winner_x, winner_y, 1)
    elif game_won == 2:
        show_winner(winner_x, winner_y, 2)

    # Refresh the window
    pygame.display.flip()

    if game_won != 0:
        pygame.time.delay(7000)
        pygame.mixer.music.unpause()
        game_won = 0