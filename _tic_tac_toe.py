import random

def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)
    print("\n")

def check_win(board, player):
    for i in range(3):
        if all([cell == player for cell in board[i]]):
            return True
        if all([board[j][i] == player for j in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]):
        return True
    if all([board[i][2 - i] == player for i in range(3)]):
        return True
    return False

def is_full(board):
    return all(cell in ['X', 'O'] for row in board for cell in row)

def get_empty_cells(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == " "]

def ai_move(board):
    empty_cells = get_empty_cells(board)
    return random.choice(empty_cells)

def play_game(vs_ai=False, scores={"X": 0, "O": 0, "Ties": 0}):
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    print_board(board)

    while True:
        if vs_ai and current_player == "O":
            row, col = ai_move(board)
            print(f"AI chooses: Row {row+1}, Column {col+1}")
        else:
            try:
                row = int(input(f"Player {current_player}, enter row (1-3): ")) - 1
                col = int(input(f"Player {current_player}, enter column (1-3): ")) - 1
            except ValueError:
                print("❌ Invalid input. Enter numbers between 1 and 3.")
                continue

            if row not in range(3) or col not in range(3):
                print("❌ Out of range! Choose row and column between 1 and 3.")
                continue

            if board[row][col] != " ":
                print("❌ Cell already taken. Try again.")
                continue

        if board[row][col] == " ":
            board[row][col] = current_player

        print_board(board)

        if check_win(board, current_player):
            print(f"🎉 Player {current_player} wins!")
            scores[current_player] += 1
            break

        if is_full(board):
            print("😐 It's a tie!")
            scores["Ties"] += 1
            break

        current_player = "O" if current_player == "X" else "X"

    print(f"📊 Scoreboard → X: {scores['X']} | O: {scores['O']} | Ties: {scores['Ties']}")
    return scores

def tic_tac_toe():
    print("🎮 Welcome to Tic Tac Toe!")
    print("1. Player vs Player")
    print("2. Player vs AI")

    while True:
        choice = input("Choose game mode (1 or 2): ")
        if choice == "1":
            vs_ai = False
            break
        elif choice == "2":
            vs_ai = True
            break
        else:
            print("❌ Invalid choice. Please select 1 or 2.")

    scores = {"X": 0, "O": 0, "Ties": 0}

    while True:
        scores = play_game(vs_ai=vs_ai, scores=scores)
        again = input("🔁 Play again? (y/n): ").lower()
        if again != 'y':
            print("👋 Thanks for playing!")
            break

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
