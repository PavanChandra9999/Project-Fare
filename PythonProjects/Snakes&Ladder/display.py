import pygame

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("Snake and Ladder Game")

# Load images
background_image = pygame.image.load('board.png')
player1_image = pygame.image.load('player1.png')
player2_image = pygame.image.load('player2.png')

# Set up player positions
player1_position = 1
player2_position = 1

# Game loop
running = True
while running:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Display the board and players
    screen.blit(background_image, (0, 0))
    screen.blit(player1_image, (50, 650))
    screen.blit(player2_image, (50, 650))
    # Define the starting position of the first player
    x1 = 50
    y1 = 650

    # Define the starting position of the second player
    x2 = 100
    y2 = 100



    # Display the player positions
    font = pygame.font.Font('freesansbold.ttf', 32)
    text1 = font.render("Player 1: {}".format(player1_position), True, (255, 255, 255))
    text2 = font.render("Player 2: {}".format(player2_position), True, (255, 255, 255))
    screen.blit(text1, (50, 550))
    screen.blit(text2, (650, 550))

    # Update the display
    pygame.display.update()

# Quit Pygame
pygame.quit()
