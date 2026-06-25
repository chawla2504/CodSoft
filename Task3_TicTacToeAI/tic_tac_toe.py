import math

board = [" " for _ in range(9)]


def print_board():
    print()
    for i in range(0, 9, 3):
        print(f" {board[i]} | {board[i + 1]} | {board[i + 2]} ")
        if i < 6:
            print("---|---|---")
    print()


def check_winner(player):
    win_patterns = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]
    ]

    for pattern in win_patterns:
        if all(board[pos] == player for pos in pattern):
            return True

    return False


def is_draw():
    return " " not in board


def minimax(is_maximizing):

    if check_winner("O"):
        return 1

    if check_winner("X"):
        return -1

    if is_draw():
        return 0

    if is_maximizing:

        best_score = -math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                score = minimax(False)
                board[i] = " "
                best_score = max(best_score, score)

        return best_score

    else:

        best_score = math.inf

        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                score = minimax(True)
                board[i] = " "
                best_score = min(best_score, score)

        return best_score


def ai_move():

    best_score = -math.inf
    move = None

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:
                best_score = score
                move = i

    board[move] = "O"


def player_move():

    while True:

        try:
            move = int(input("Enter position (1-9): ")) - 1

            if 0 <= move <= 8 and board[move] == " ":
                board[move] = "X"
                break

            else:
                print("Invalid move! Try again.")

        except ValueError:
            print("Please enter a number between 1 and 9.")


def reset_board():
    global board
    board = [" " for _ in range(9)]


def play_again():

    while True:

        choice = input("\nPlay Again? (Y/N): ").strip().upper()

        if choice == "Y":
            return True

        elif choice == "N":
            print("\nThanks for playing!")
            return False

        else:
            print("Please enter Y or N.")


print("""
=================================
        TIC TAC TOE AI
=================================

Positions:

1 | 2 | 3
---------
4 | 5 | 6
---------
7 | 8 | 9

You = X
AI  = O
""")

while True:

    reset_board()

    while True:

        print_board()

        player_move()

        if check_winner("X"):
            print_board()
            print("🎉 You Win!")
            break

        if is_draw():
            print_board()
            print("🤝 Draw!")
            break

        ai_move()

        if check_winner("O"):
            print_board()
            print("🤖 AI Wins!")
            break

        if is_draw():
            print_board()
            print("🤝 Draw!")
            break

    if not play_again():
        break