# Define the size of the board
board_size = 10

# Define the positions of the ladders and snakes
ladders = {4: 16, 23: 34, 28: 56, 35: 59, 40: 82, 63: 72, 68: 77}
snakes = {13: 7, 22: 2, 25: 14, 42: 24, 51: 31, 53: 26, 79: 17, 87: 55, 98: 77}

# Create a list to represent each row of the board
board_rows = []
for row in range(board_size):
    if row % 2 == 0:
        # Even rows go from left to right
        board_row = list(range(row * board_size + 1, (row + 1) * board_size + 1))
    else:
        # Odd rows go from right to left
        board_row = list(range((row + 1) * board_size, row * board_size, -1))
    board_rows.append(board_row)

# Print the board
for row in board_rows[::-1]:
    for position in row:
        if position in ladders:
            # Print a ladder symbol
            print(f" L{position}->{ladders[position]:02d} ", end="")
        elif position in snakes:
            # Print a snake symbol
            print(f" S{position}->{snakes[position]:02d} ", end="")
        else:
            # Print the position number
            print(f"{position:02d}", end="")
        print(" | ", end="")
    print("\n" + "-" * 4 * board_size)
