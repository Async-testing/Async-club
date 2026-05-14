def print_board(board):
    print("\n")
    for i in range(3):
        print(" {} | {} | {} ".format(board[i*3], board[i*3+1], board[i*3+2]))
        if i < 2:
            print("---+---+---")
    print("\n")


def check_winner(board, player):
    win_positions = [
        (0, 1, 2),
        (3, 4, 5),
        (6, 7, 8),
        (0, 3, 6),
        (1, 4, 7),
        (2, 5, 8),
        (0, 4, 8),
        (2, 4, 6),
    ]
    return any(board[a] == board[b] == board[c] == player for a, b, c in win_positions)


def is_draw(board):
    return all(cell != ' ' for cell in board)


def get_move(player, board):
    while True:
        try:
            move = int(input(f"Player {player}, choose a position (1-9): "))
            if move < 1 or move > 9:
                print("Please choose a number between 1 and 9.")
                continue
            if board[move - 1] != ' ':
                print("That position is already taken. Pick another one.")
                continue
            return move - 1
        except ValueError:
            print("Invalid input. Enter a number between 1 and 9.")


def main():
    board = [' '] * 9
    current_player = 'X'

    print("Welcome to Tic Tac Toe!")
    print("Positions are numbered 1-9 as follows:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 \n")

    while True:
        print_board(board)
        move = get_move(current_player, board)
        board[move] = current_player

        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!\n")
            break

        if is_draw(board):
            print_board(board)
            print("It's a draw!\n")
            break

        current_player = 'O' if current_player == 'X' else 'X'

    print("Thanks for playing!")


if __name__ == '__main__':
    main()
