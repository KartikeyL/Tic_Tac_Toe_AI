import random

def display_board(board):
    """Display the Tic-Tac-Toe board."""
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    """Check if the specified player has won."""
    for row in board:
        if all(cell == player for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True
    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True
    return False

def check_draw(board):
    """Check if the game is a draw."""
    return all(cell != " " for row in board for cell in row)

def get_empty_cells(board):
    """Return a list of empty cells on the board."""
    return [(row, col) for row in range(3) for col in range(3) if board[row][col] == " "]

def minimax(board, depth, is_maximizing):
    """Minimax algorithm implementation."""
    if check_winner(board, "X"):
        return -10 + depth, None
    elif check_winner(board, "O"):
        return 10 - depth, None
    elif check_draw(board):
        return 0, None

    if is_maximizing:
        best_score = -float('inf')
        best_move = None
        for row, col in get_empty_cells(board):
            board[row][col] = "O"
            score, _ = minimax(board, depth + 1, False)
            board[row][col] = " "
            if score > best_score:
                best_score = score
                best_move = (row, col)
        return best_score, best_move
    else:
        best_score = float('inf')
        best_move = None
        for row, col in get_empty_cells(board):
            board[row][col] = "X"
            score, _ = minimax(board, depth + 1, True)
            board[row][col] = " "
            if score < best_score:
                best_score = score
                best_move = (row, col)
        return best_score, best_move

def main():
    """Main function to run the game."""
    board = [[" "]*3 for _ in range(3)]
    display_board(board)
    while True:
        player_row, player_col = map(int, input("Enter your move (row col): ").split())
        if board[player_row][player_col] != " ":
            print("Cell already occupied. Try again.")
            continue
        board[player_row][player_col] = "X"
        display_board(board)
        if check_winner(board, "X"):
            print("Congratulations! You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break
        _, ai_move = minimax(board, 0, True)
        board[ai_move[0]][ai_move[1]] = "O"
        print(f"AI plays at {ai_move}")
        display_board(board)
        if check_winner(board, "O"):
            print("AI wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    main()
