def print_board(board):
    for row in board:
        print(" | ".join(row))  # Printing each row of the board with "|" between symbols
        print("-" * 9)  # Horizontal lines between rows

def check_winner(board, player):
    # Checking rows and columns
    for i in range(3):
        if all([spot == player for spot in board[i]]) or all([spot == player for spot in [board[j][i] for j in range(3)]]):
            return True
    # Checking diagonals
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def is_board_full(board):
    return all([spot != " " for row in board for spot in row])  # Checking if all cells of the board are filled

def get_move(board):
    while True:
        move = input("Enter your move (row and column): ").split()
        if len(move) == 2 and move[0].isdigit() and move[1].isdigit():
            row, col = int(move[0]), int(move[1])
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":  # Checking the validity of the input move
                return row, col
        print("Invalid move. Please try again.")

def tic_tac_toe():
    board = [[" " for _ in range(3)] for _ in range(3)]  # Creating an empty board
    current_player = "X"  # Current player

    while True:
        print_board(board)  # Printing the current board
        print(f"Player {current_player}'s turn.")  # Displaying the current player's turn
        row, col = get_move(board)  # Getting the player's move
        board[row][col] = current_player  # Recording the move on the board

        if check_winner(board, current_player):  # Checking if the player wins
            print_board(board)
            print(f"Player {current_player} wins!")  # Displaying the winning player
            break
        elif is_board_full(board):  # Checking for a tie
            print_board(board)
            print("The game is a tie!")  # Displaying a tie
            break

        current_player = "O" if current_player == "X" else "X"  # Switching player turns

# Running the game
tic_tac_toe()

# Name of the programmer: Maryam Jamali
# Email address: m.jamali16@yahoo.com
# GitHub address: https://github.com/MaryaJamali
