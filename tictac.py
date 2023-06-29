# Tic Tac Toe game in Python

board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]

# Display the Tic Tac Toe board
def display_board():
    print(f'{board[0][0]} | {board[0][1]} | {board[0][2]}')
    print(f'{board[1][0]} | {board[1][1]} | {board[1][2]}')
    print(f'{board[2][0]} | {board[2][1]} | {board[2][2]}')
    print()

# Check if the game is over
def game_over():
    # Check rows
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != '-':
            return True

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != '-':
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '-':
        return True
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '-':
        return True

    return False

# Play the game
player = 'X'
while not game_over():
    display_board()
    row = int(input(f'Player {player}, choose a row (0-2): '))
    col = int(input(f'Player {player}, choose a column (0-2): '))

    if board[row][col] == '-':
        board[row][col] = player
        player = 'O' if player == 'X' else 'X'
    else:
        print('That spot is already taken. Try again.')

# Game over
display_board()
winner = 'O' if player == 'X' else 'X'
print(f'Congratulations! Player {winner} wins!')
