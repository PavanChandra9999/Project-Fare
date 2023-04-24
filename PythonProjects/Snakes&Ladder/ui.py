import pygame

# Initialize pygame
pygame.init()

# Set the screen dimensions
screen_width = 800
screen_height = 600

# Set the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Set the font for text
font = pygame.font.SysFont(None, 30)

# Set the caption for the game
pygame.display.set_caption("Snakes and Ladders")

# Create the screen
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the game clock
clock = pygame.time.Clock()

# Draw the board
def draw_board():
    # Draw the grid
    for i in range(10):
        for j in range(10):
            if (i + j) % 2 == 0:
                pygame.draw.rect(screen, white, (i * 60, j * 60, 60, 60))
            else:
                pygame.draw.rect(screen, black, (i * 60, j * 60, 60, 60))

    # Draw the snakes
    snakes = {13: 7, 22: 2, 25: 14, 42: 24, 51: 31, 53: 26, 79: 17, 87: 55, 98: 77}
    for start, end in snakes.items():
        start_row = (start - 1) // 10
        start_col = (start - 1) % 10
        end_row = (end - 1) // 10
        end_col = (end - 1) % 10
        pygame.draw.line(screen, red, ((start_col + 0.5) * 60, (start_row + 0.5) * 60), ((end_col + 0.5) * 60, (end_row + 0.5) * 60), 10)

    # Draw the ladders
    ladders = {4: 16, 23: 34, 28: 56, 35: 59, 40: 82, 63: 72, 68: 89}
    for start, end in ladders.items():
        start_row = (start - 1) // 10
        start_col = (start - 1) % 10
        end_row = (end - 1) // 10
        end_col = (end - 1) % 10
        pygame.draw.line(screen, green, ((start_col + 0.5) * 60, (start_row + 0.5) * 60), ((end_col + 0.5) * 60, (end_row + 0.5) * 60), 10)

# Display the player positions
def display_positions():
    screen.blit(background_image, (0, 0))
    for i in range(num_players):
        player = players[i]
        player_image = player_images[i]
        x, y = get_player_position(player.position)
        screen.blit(player_image, (x, y))
        font = pygame.font.Font('freesansbold.ttf', 32)
        text = font.render("Player {}: {}".format(i+1, player.position), True, (255, 255, 255))
        screen.blit(text, (x, y-30))
    pygame.display.update()


