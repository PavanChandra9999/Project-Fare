import random

# Define the positions of the ladders and snakes
ladders = {4: 16, 23: 34, 28: 56, 35: 59, 40: 82, 63: 72, 68: 77}
snakes = {13: 7, 22: 2, 25: 14, 42: 24, 51: 31, 53: 26, 79: 17, 87: 55, 98: 77}

# Set the starting position of the player
player_position = 0


# Play the game until the player reaches the end
while player_position < 100:
    # Roll the dice and move the player
    dice_roll = random.randint(1, 6)
    player_position += dice_roll
    
    # Check if the player has landed on a ladder or a snake
    if player_position in ladders:
        player_position = ladders[player_position]
        print("You climbed a ladder! You're now at position", player_position)
    elif player_position in snakes:
        player_position = snakes[player_position]
        print("You got bitten by a snake! You're now at position", player_position)
    
    # Check if the player has reached the end of the board
    if player_position == 100:
        print("You rolled a", dice_roll, "and landed on position", player_position)
        print("Congratulations, you won!")

    elif player_position > 100:
        player_position -= dice_roll
        print("You rolled a", dice_roll, "It is INVALID and now You're at position ", player_position)
        

    else:
        print("You rolled a", dice_roll, "and landed on position", player_position)
