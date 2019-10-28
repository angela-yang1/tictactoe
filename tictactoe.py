class Player:
    def __init__(self, n, s):
        self.number = n
        self.symbol = s


# Handling different input methods for different Python versions
input_func = None
try:
    input_func = raw_input
except NameError:
    input_func = input


def display_board():
    for row in board:
        print(" ".join(row))
    print("")


def switch_player():
    player1 = Player(1, "X")
    player2 = Player(2, "O")
    current_player = player1 if turn % 2 == 0 else player2
    return current_player


def get_user_input():
    while True:
        player_input = input_func("Player {} enter a coord x, y to place your {} or enter 'q' to give up: ".format(
            current_player.number, current_player.symbol))
        print("")

        if (player_input.lower() == "q"):
            print("You've quit the game!")
            exit()

        player_move = player_input.split(",")

        try:
            x, y = map(int, player_move)
        except ValueError:
            print("Invalid input! Please try again. \n")
            continue

        if x > 3 or y > 3 or x < 1 or y < 1:
            print(
                "The coordinates you have entered are outside of the range! Please try again. \n")
            continue

        if board[x - 1][y - 1] != ".":
            print("Oh no, a piece is already at this place! Please try again. \n")
            continue

        return x, y


def check_win(x, y):
    diag_comb_1 = [board[0][0], board[1][1], board[2][2]]
    diag_comb_2 = [board[0][2], board[1][1], board[2][0]]
    row_win = all(current_player.symbol == cell for cell in board[x - 1])
    col_win = all(current_player.symbol == row[y - 1] for row in board)
    diag_win = all(current_player.symbol == cell for cell in diag_comb_1) or all(
        current_player.symbol == cell for cell in diag_comb_2)

    if row_win or col_win or diag_win:
        print("Move accepted. Well done player {}, you've won the game! \n".format(
            current_player.number))
        display_board()
        exit()


# Global variables
turn = 0
current_player = switch_player()
board = [
    ['.', '.', '.'],
    ['.', '.', '.'],
    ['.', '.', '.']
]

# Initial welcome message
print("Welcome to Tic Tac Toe! \n")
print("Here's the current board: \n")
display_board()

# Beginning of the game loop
while True:
    x, y = get_user_input()
    board[x - 1][y - 1] = current_player.symbol
    turn += 1

    if turn > 4:
        check_win(x, y)
    if turn == 9:
        print("Move accepted, it's a draw! \n")
        display_board()
        exit()

    print("Move accepted, here's the current board: \n")
    display_board()
    current_player = switch_player()
