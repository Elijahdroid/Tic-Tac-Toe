def initialise_board():
    first_board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    player1 = input("Which marker do you want to be, ['X' or 'O']: ")
    player2 = ""
    if player1 == "X":
        player2 = "O"
    elif player1 == "O":
        player2 = "X"
    else:
        player1 = input("Please enter the right letter, ['X' or 'O']")
        initialise_board()
    print(f"player1 is '{player1}' and player2 is '{player2}'")
    return first_board


def display_board(board):
    for i in range(3):
        for j in range(3):
            if j == 2:
                print(board[i][j], end='')
            else:
                print(board[i][j], end=' | ')
        print()
        print('--|---|---')
    print("\n")


def update_board(player_marker, position, board):
    if board[position // 3][position % 3] == 'O' or board[position // 3][position % 3] == 'X':
        print("Sorry this has already been taken. Please enter again")
        get_player_move(player_marker, board)
    else:
        board[position // 3][position % 3] = player_marker
        player_marker = switch_player(player_marker)
        check_winner(board)
        print(f"'{player_marker}' turn")


def switch_player(player_marker):
    if player_marker == "X":
        player_marker = "O"
    else:
        player_marker = "X"
    return player_marker


def get_player_move(player_marker, board):
    display_board(board)
    ask = int(input(f"Enter a number which is assigned to the board - [0-8], '{player_marker}': "))
    if 0 <= ask <= 8:
        update_board(player_marker, ask, board)
        check_winner(board)
    else:
        print("Sorry, this is not a available number. Please try again")
        get_player_move(player_marker, board)


def check_tie(board):
    board_full = []
    for i in range(0, 9):
        if board[i // 3][i % 3] != i:
            board_full.append(i)
    if len(board_full) == 9:
        display_board(board)
        announce_tie()


def check_winner(board):
    if board[0][0] == board[0][1] == board[0][2] == "X":
        display_board(board)
        announce_winner("X")
    elif board[1][0] == board[1][1] == board[1][2] == "X":
        display_board(board)
        announce_winner("X")
    elif board[2][0] == board[2][1] == board[2][2] == "X":
        display_board(board)
        announce_winner("X")
    elif board[0][0] == board[1][0] == board[2][0] == "X":
        display_board(board)
        announce_winner("X")
    elif board[0][1] == board[1][1] == board[2][1] == "X":
        display_board(board)
        announce_winner("X")
    elif board[0][2] == board[1][2] == board[2][2] == "X":
        display_board(board)
        announce_winner("X")
    elif board[0][0] == board[1][1] == board[2][2] == "X":
        display_board(board)
        announce_winner("X")
    elif board[0][2] == board[1][1] == board[2][0] == "X":
        display_board(board)
        announce_winner("X")
    elif board[0][0] == board[0][1] == board[0][2] == "O":
        display_board(board)
        announce_winner("O")
    elif board[1][0] == board[1][1] == board[1][2] == "O":
        display_board(board)
        announce_winner("O")
    elif board[2][0] == board[2][1] == board[2][2] == "O":
        display_board(board)
        announce_winner("O")
    elif board[0][0] == board[1][0] == board[2][0] == "O":
        display_board(board)
        announce_winner("O")
    elif board[0][1] == board[1][1] == board[2][1] == "O":
        display_board(board)
        announce_winner("O")
    elif board[0][2] == board[1][2] == board[2][2] == "O":
        display_board(board)
        announce_winner("O")
    elif board[0][0] == board[1][1] == board[2][2] == "O":
        display_board(board)
        announce_winner("O")
    elif board[0][2] == board[1][1] == board[2][0] == "O":
        display_board(board)
        announce_winner("O")
    else:
        check_tie(board)


def announce_winner(winner_marker):
    print(f"'{winner_marker}' has won")
    exit()


def announce_tie():
    print("It is a tie")
    exit()


def play_game():
    player_marker = "X"
    board = initialise_board()
    for i in range(0, 10):
        get_player_move(player_marker, board)
        player_marker = switch_player(player_marker)


play_game()