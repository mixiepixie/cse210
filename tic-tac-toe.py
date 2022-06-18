'''
Michal Garcia
CSE 210 Week 1 Prove assignment
Tic-Tac-Toe Game :)
'''


def main():
    turn_num = 0
    player_1 = input("Player 1 please enter your name: ")
    player_2 = input("Player 2 please enter your name: ")
    print(f'{player_1} you are playing as "x"')
    print(f'{player_2} you are playing as "o"')
    board = write_interface()
    display_board(board)
    while not(cross_win(board)) or is_a_draw(board):
        if turn_num % 2 == 0:
            turn_num += 1
            make_move_x(player_1, board)
            cross_win(board)
            display_board(board)
            if cross_win(board):
                print(f"Yay! {player_1} wins!")
                break
            if is_a_draw(board):
                print('it was a tie. ')
                break

        else:
            turn_num += 1
            make_move_y(player_2, board)
            cross_win(board)
            display_board(board)
            if cross_win(board):
                print(f"Yay! {player_2} wins!")
                break
            if is_a_draw(board):
                print('it was a tie. ')
                break


def is_a_draw(board):
    for square in range(9):
        if board[square] != "x" and board[square] != "o":
            return False
    return True


def write_interface():
    board = []
    for square in range(9):
        board.append(square + 1)
    return board


def cross_win(board):

    return(board[0] == board[1] == board[2] or
           board[3] == board[4] == board[5] or
           board[6] == board[7] == board[8] or
           board[0] == board[3] == board[6] or
           board[1] == board[4] == board[7] or
           board[2] == board[5] == board[8] or
           board[0] == board[4] == board[8] or
           board[2] == board[4] == board[6])


def display_board(board):
    print()
    print(f"{board[0]}|{board[1]}|{board[2]}")
    print('-+-+-')
    print(f"{board[3]}|{board[4]}|{board[5]}")
    print('-+-+-')
    print(f"{board[6]}|{board[7]}|{board[8]}")
    print()


def make_move_x(player_1, board):
    square = int(input(f"{player_1}'s turn to choose a square (1-9): "))
    player_1_symbol = "x"
    board[square - 1] = player_1_symbol


def make_move_y(player_2, board):
    square = int(input(f"{player_2}'s turn to choose a square (1-9): "))
    player_2_symbol = "o"
    board[square - 1] = player_2_symbol


if __name__ == "__main__":
    main()
