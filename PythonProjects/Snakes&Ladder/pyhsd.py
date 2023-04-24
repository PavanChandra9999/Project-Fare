import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Define the size of the board
board_size = 10

# Define the positions of the ladders and snakes
ladders = {4: 16, 23: 34, 28: 56, 35: 59, 40: 82, 63: 72, 68: 77}
snakes = {13: 7, 22: 2, 25: 14, 42: 24, 51: 31, 53: 26, 79: 17, 87: 55, 98: 77}

# Initialize Pygame
pygame.init()

# Set the width and height of the screen (including margins)
width = 800
height = 600
margin = 50
screen = pygame.display.set_mode((width, height))

# Set the title of the game window
pygame.display.set_caption("Snake and Ladder")

# Create a font for the player's score
font = pygame.font.SysFont(None, 48)

# Define a function to draw the board
def draw_board():
    # Clear the screen
    screen.fill(WHITE)

    # Draw the board squares
    for row in range(board_size):
        for col in range(board_size):
            x = col * (width - 2 * margin) / board_size + margin
            y = (board_size - 1 - row) * (height - 2 * margin) / board_size + margin
            pygame.draw.rect(screen, BLACK, [x, y, (width - 2 * margin) / board_size, (height - 2 * margin) / board_size], 2)

    # Draw the ladders
    for start, end in ladders.items():
        start_col = (start - 1) % board_size
        start_row = (start - 1) // board_size
        end_col = (end - 1) % board_size
        end_row = (end - 1) // board_size
        start_x = start_col * (width - 2 * margin) / board_size + margin + (width - 2 * margin) / board_size / 2
        start_y = (board_size - 1 - start_row) * (height - 2 * margin) / board_size + margin + (height - 2 * margin) / board_size / 2
        end_x = end_col * (width - 2 * margin) / board_size + margin + (width - 2 * margin) / board_size / 2
        end_y = (board_size - 1 - end_row) * (height - 2 * margin) / board_size + margin + (height - 2 * margin) / board_size / 2
        pygame.draw.line(screen, RED, [start_x, start_y], [end_x, end_y], 5)

    # Draw the snakes
    for start, end in snakes.items():
        start_col = (start - 1) % board_size
        start_row = (start - 1) // board_size
        end_col = (end - 1) % board_size
        end_row = (end - 1) // board_size
        start_x = start_col * (width - 2 * margin) / board_size + margin + (width - 2 * margin) / board_size / 2
        start_y = (board_size - 1 - start_row) * (height - 2 * margin) / board_size + margin + (height - 2 * margin) / board_size / 2
        end_x = end_col * (width - 2 * margin) / board_size + margin + (width - 2 * margin) / board_size / 2
        end_y = (board_size - 1 - end_row) * (height - 2 * margin) / board_size + margin + (height - 2 * margin) / board_size / 2
        pygame.draw.line(screen, BLACK, [start_x, start_y], [end_x, end_y], 5)

    # Update the screen
    pygame.display.update()

    # Set the initial score
    score = 0

    # Loop until the game is over
    game_over = False
    while not game_over:
        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # Roll the dice
                    dice_roll = random.randint(1, 6)

                    # Move the player
                    player_pos += dice_roll

                    # Check for ladders and snakes
                    if player_pos in ladders:
                        player_pos = ladders[player_pos]
                    elif player_pos in snakes:
                        player_pos = snakes[player_pos]

                    # Check if the player has won
                    if player_pos >= board_size ** 2:
                        game_over = True

                    # Update the score
                    score += 1

        # Draw the board and the player
        draw_board()
        player_col = (player_pos - 1) % board_size
        player_row = (player_pos - 1) // board_size
        player_x = player_col * (width - 2 * margin) / board_size + margin + (width - 2 * margin) / board_size / 2
        player_y = (board_size - 1 - player_row) * (height - 2 * margin) / board_size + margin + (height - 2 * margin) / board_size / 2
        pygame.draw.circle(screen, RED, [int(player_x), int(player_y)], 20)

        # Draw the score
        score_text = font.render("Score: {}".format(score), True, BLACK)
        screen.blit(score_text, [10, 10])

        # Update the screen
        pygame.display.update()

# Quit Pygame
pygame.quit()


