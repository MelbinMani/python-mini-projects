from random import choice


def display_board(board):

    # Display the board. row by row.

    for row in board:
        print("+-------+-------+-------+")
        print("|       |       |       |")
        print(f"|   {row[0]}   |   {row[1]}   |   {row[2]}   |")
        print("|       |       |       |")
    print("+-------+-------+-------+")

# Return a list of free fields on the board.So that we can check for valid moves.


def free_fields(board):
    free_fields = [(i, j) for i in range(3)
                   for j in range(3) if board[i][j] == ' ']
    return free_fields

# Get the user's valid move.


def user(board):
    while True:

        available = [i * 3 + j + 1 for i, j in free_fields(board)]

        # available = [i * 3 + j + 1 for i in range(3)
        #              for j in range(3) if board[i][j] == ' ']

        move = input(f"Enter your move (1-9) from available {available}: ")
        if move.isdigit() and int(move) in available:
            move = int(move) - 1
            return divmod(move, 3)
        else:
            print("Invalid input. Please enter a valid number.")

# Computer's move - random selection from available fields.


def computer(board):
    available = free_fields(board)
    if available:
        return choice(available)

# Apply the move to the board.The sign is either 'O' or 'X' assigned in the play_game .The position is a tuple (row, col).


def move(board, position, sign):
    row, col = position
    board[row][col] = sign


def victory_for(board, sign):
    for row in board:
        if all(cell == sign for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == sign for row in range(3)):
            return True
    if all(board[i][i] == sign for i in range(3)) or \
       all(board[i][2 - i] == sign for i in range(3)):
        return True


def check_draw(board):
    return all(cell != ' ' for row in board for cell in row)


def play_game():
    board = [[' ' for i in range(3)] for j in range(3)]
    current_sign = 'O'  # Human starts
    while True:
        display_board(board)

        if current_sign == 'O':
            position = user(board)
        else:
            position = computer(board)

        move(board, position, current_sign)

        if victory_for(board, current_sign):
            display_board(board)
            print(f"{'You' if current_sign == 'O' else 'Computer'} win!")
            break

        if check_draw(board):
            display_board(board)
            print("It's a draw!")
            break

        current_sign = 'X' if current_sign == 'O' else 'O'


def main():
    while True:
        play_game()
        replay = input("Do you want to play again? (y/n): ").lower()
        if replay != 'y':
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
