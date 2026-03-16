import csv

def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("--+---+--")
    print("\n")


def check_winner(board):
    # Rows, columns, diagonals
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return board[i][0]
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return board[0][i]

    if board[0][0] == board[1][1] == board[2][2] != " ":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] != " ":
        return board[0][2]

    return None


def is_full(board):
    for row in board:
        if " " in row:
            return False
    return True


def play_game(player_x, player_o, scores):
    board = [[" " for _ in range(3)] for _ in range(3)]
    current = "X"

    while True:
        print_board(board)

        player_name = player_x if current == "X" else player_o
        print(f"{player_name}'s turn ({current})")

        try:
            row = int(input("Enter row (0-2): "))
            col = int(input("Enter col (0-2): "))
        except ValueError:
            print("Invalid input. Try again.")
            continue

        if row not in range(3) or col not in range(3) or board[row][col] != " ":
            print("Invalid move. Try again.")
            continue

        board[row][col] = current

        winner = check_winner(board)
        if winner:
            print_board(board)
            winner_name = player_x if winner == "X" else player_o
            print(f"{winner_name} wins!")
            scores[winner_name] += 1
            return

        if is_full(board):
            print_board(board)
            print("It's a tie!")
            return

        current = "O" if current == "X" else "X"


def save_scores(scores):
    with open("scores.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Player", "Score"])
        for player, score in scores.items():
            writer.writerow([player, score])


def main():
    print("Welcome to Tic Tac Toe!")

    player_x = input("Enter name for Player X: ")
    player_o = input("Enter name for Player O: ")

    scores = {
        player_x: 0,
        player_o: 0
    }

    while True:
        play_game(player_x, player_o, scores)

        print("\nCurrent Scores:")
        for player, score in scores.items():
            print(f"{player}: {score}")

        again = input("Play again? (y/n): ").lower()
        if again != "y":
            save_scores(scores)
            print("Scores saved to scores.csv. Goodbye!")
            break


if __name__ == "__main__":
    main()