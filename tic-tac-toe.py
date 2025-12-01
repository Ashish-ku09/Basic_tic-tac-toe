# tic_tac_toe.py

BOARD_SIZE = 3

def create_board():
    return [[" " for _ in range(BOARD_SIZE)] for _ in range(BOARD_SIZE)]

def print_board(board):
    print("\n  " + "   ".join(str(i + 1) for i in range(BOARD_SIZE)))
    for idx, row in enumerate(board):
        row_str = " | ".join(row)
        print(f"{idx + 1} {row_str}")
        if idx < BOARD_SIZE - 1:
            print("  " + "-" * (BOARD_SIZE * 4 - 3))
    print()

def is_valid_move(board, row, col):
    if not (0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE):
        return False
    return board[row][col] == " "

def check_winner(board):
    lines = []

    # Rows and columns
    lines.extend(board)
    lines.extend([[board[r][c] for r in range(BOARD_SIZE)] for c in range(BOARD_SIZE)])

    # Diagonals
    diag1 = [board[i][i] for i in range(BOARD_SIZE)]
    diag2 = [board[i][BOARD_SIZE - 1 - i] for i in range(BOARD_SIZE)]
    lines.append(diag1)
    lines.append(diag2)

    for line in lines:
        if line.count(line[0]) == BOARD_SIZE and line[0] != " ":
            return line[0]

    return None

def is_board_full(board):
    return all(cell != " " for row in board for cell in row)

def switch_player(current_player):
    return "O" if current_player == "X" else "X"

def get_player_move(player):
    while True:
        move = input(f"Player {player}, enter your move as row,col (e.g., 1,3): ")
        try:
            row_str, col_str = move.split(",")
            row = int(row_str.strip()) - 1
            col = int(col_str.strip()) - 1
            return row, col
        except ValueError:
            print("Invalid format. Please enter row and column as numbers separated by a comma.")

def play_game():
    board = create_board()
    current_player = "X"

    print("Welcome to Tic-Tac-Toe!")
    print("Players take turns to place X and O on the board.")
    print("To make a move, enter row,col (for example: 2,3).")

    while True:
        print_board(board)
        row, col = get_player_move(current_player)

        if not is_valid_move(board, row, col):
            print("Invalid move. Try again.")
            continue

        board[row][col] = current_player

        winner = check_winner(board)
        if winner:
            print_board(board)
            print(f"Player {winner} wins! 🎉")
            break

        if is_board_full(board):
            print_board(board)
            print("It's a tie! 🤝")
            break

        current_player = switch_player(current_player)

if __name__ == "__main__":
    play_game()
