## Description:
A simple Tic Tac Toe game ( ❌ , ⭕ ) written in the popular Python language and run as a text.
In this game, two players alternately enter their turns with "X" and "O" marks on a 3x3 table.
The goal of this game is for one of the players to place their three distinctive marks in a row, column or diagonal of the table and win.
If all the houses on the table are filled and no one wins, the game ends in a draw.<br/>
This code uses functions such as ```print_board``` , ```check_winner``` , ```is_board_full``` ,```get_move``` and ```tic_tac_toe```.
## How to use:
1. Simulate your repository: ```git clone https://github.com/MaryaJamali/Tic-Tac-Toe-Game.git```
2. Run the program
## Instructions:
Various functions are defined in this code :<br/><br/>
```def print_board(board):```
This function prints the game board. "X" and "O" marks and the emptyness of each house are displayed in the table. Each line is separated by a horizontal line from the "-" sign.<br/><br/>
```def check_winner(board, player):```
This function checks whether the current player has won or not. For this purpose, first the rows and columns of the table and then its two diagonals are checked. If a player has filled all the squares of one of these components with his mark, that player wins.<br/><br/>
```def is_board_full(board):```
This function checks if the board is full, meaning the game ends in a draw.<br/><br/>
```def get_move(board):```
This function takes input from the user, which includes the row and column numbers to place the mark. Input must be two positive integers indicating a valid position in the table.<br/><br/>
```def tic_tac_toe():```
This function performs the main execution of the game. First, an empty table is created and the first turn belongs to player "X". Then alternately the players choose their turn and make their valid move. Then the winner or draw of the game is checked and if necessary, the game ends.<br/><br/>
Finally, the ```tic_tac_toe()``` function is called and the game starts.
## Author:
Maryam Jamali 💙
