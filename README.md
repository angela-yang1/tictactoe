# Tic Tac Toe
A console based Tic Tac Toe game, that allows two human players to play on a 3 x 3 board.

## To start the game
> Note: Python 2.7.x or 3.x is required to run the game.

Open the terminal and navigate to the same directory as `tictactoe.py`.

##### For Python 3:
Run `python3 tictactoe.py` 

##### For Python 2.7:
Run `python tictactoe.py`

## How to play
Enter `x`(row) and `y`(column) coordinates to make a move:
```
   1 2 3 y
1  . . .
2  . . .
3  . . .
x
```

* Requires two players, player 1 always starts the game
  - Player 1 = X
  - Player 2 = O
* Each player takes a turn to place "X" or "O" on the selected field
* The game ends when:
  - ***A player wins***, by placing their "X" or "O", three in a row, column or diagonally
  - ***A draw happens***, when all fields are taken on the board
  - ***A player quits the game***, by entering 'q' as their input
  
## Example Game

```
Welcome to Tic Tac Toe!

Here's the current board:

. . .
. . .
. . .

Player 1 enter a coord x,y to place your X or enter 'q' to give up: 1,1

Move accepted, here's the current board:

X . .  
. . . 
. . .

Player 2 enter a coord x,y to place your O or enter 'q' to give up: 1,1

Oh no, a piece is already at this place! Try again...

Player 2 enter a coord x,y to place your O or enter 'q' to give up: 1,3

Move accepted, here's the current board:

X . O  
. . . 
. . .

Player 1 enter a coord x,y to place your X or enter 'q' to give up: 2,1

Move accepted, here's the current board:

X . O  
X . . 
. . .

Player 2 enter a coord x,y to place your O or enter 'q' to give up: 2,2

Move accepted, here's the current board:

X . O  
X O . 
. . .

Player 1 enter a coord x,y to place your X or enter 'q' to give up: 3,1

Move accepted. Well done player 1, you've won the game!  

X . O  
X O . 
X . .
```
