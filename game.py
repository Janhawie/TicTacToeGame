# Function to initialize the game board
def initialize_board():
    return [[' ' for _ in range(3)] for _ in range(3)]

# Function to print the game board with emojis and better formatting
def print_board(board):
    symbol_map = {'X': '❌', 'O': '⭕', ' ': '   '}
    for i, row in enumerate(board):
        print(" | ".join(symbol_map[cell] for cell in row))
        if i < 2:
            print("----------------")

# Function to check if the current player has won
def check_win(board, player):
    for row in board:
        if row.count(player) == 3:
            return True
    for col in range(3):
        if [board[row][col] for row in range(3)].count(player) == 3:
            return True
    if [board[i][i] for i in range(3)].count(player) == 3:
        return True
    if [board[i][2 - i] for i in range(3)].count(player) == 3:
        return True
    return False

# Function to check for a draw
def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)

# Function to handle the player's move
def player_move(board, player_symbol, player_name):
    while True:
        try:
            row = int(input(f"{player_name}, enter row (1-3): ")) - 1
            col = int(input(f"{player_name}, enter column (1-3): ")) - 1

            if 0 <= row <= 2 and 0 <= col <= 2:
                if board[row][col] == ' ':
                    board[row][col] = player_symbol
                    break
                else:
                    print("This spot is already taken, try again.")
            else:
                print("Row and column must be between 1 and 3.")
        except ValueError:
            print("Invalid input. Please enter numeric values between 1 and 3.")

# Main game function
def main():
    board = initialize_board()
    current_player = 'X'
    player_names = {'X': "Player 1", 'O': "Player 2"}

    while True:
        print_board(board)
        player_move(board, current_player, player_names[current_player])

        if check_win(board, current_player):
            print_board(board)
            print(f"{player_names[current_player]} wins! 🎉")
            break

        if check_draw(board):
            print_board(board)
            print("It's a draw! 🤝")
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == "__main__":
    main()
