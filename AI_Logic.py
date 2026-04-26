def initialise_board():
    first_board = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    player1 = "X"
    player2 = "O"
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
    if player_marker == "O":
        position = find_best_move(board)
        update_board(player_marker, position, board)
    else:
        ask = int(input(f"Enter a number which is assigned to the board - [0-8], '{player_marker}': "))
        if 0 <= ask <= 8:
            update_board(player_marker, ask, board)
        else:
            print("Sorry, this is not a available number. Please try again")
            get_player_move(player_marker, board)


def evaluate_board(board):
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2]:
            if board[row][0] == 'O':
                return +10
            elif board[row][0] == 'X':
                return -10
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col]:
            if board[0][col] == 'O':
                return +10
            elif board[0][col] == 'X':
                return -10
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'O':
            return +10
        elif board[0][0] == 'X':
            return -10
    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'O':
            return +10
        elif board[0][2] == 'X':
            return -10


def min_and_max(board, depth, is_maximising):
    score = evaluate_board(board)
    if score == -10:
        return score + depth
    elif score == 10:
        return score - depth
    if check_tie(board):
        return 0
    if is_maximising:
        best = -1000
        for i in range(3):
            for j in range(3):
                if board[i][j] not in ["X", "O"]:
                    board[i][j] = "O"
                    best = max(best, min_and_max(board, depth+1, is_maximising=False))
                    board[i][j] = i * 3 + j
        return best
    else:
        best = 1000
        for i in range(3):
            for j in range(3):
                if board[i][j] not in ["X", "O"]:
                    board[i][j] = "X"
                    best = min(best, min_and_max(board, depth+1, is_maximising=True))
                    board[i][j] = i * 3 + j
        return best


def find_best_move(board):
    best_value = -1000
    best_move = (-1, -1)
    for i in range(3):
        for j in range(3):
            if board[i][j] not in ["X", "O"]:
                board[i][j] = "O"
                move_value = min_and_max(board, 0, False)
                board[i][j] = i * 3 + j
                if move_value > best_value:
                    best_move = (i, j)
                    best_value = move_value
    return (best_move[0] * 3) + best_move[1]


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


def check_tie(board):
    board_full = []
    for i in range(0, 9):
        if board[i // 3][i % 3] != i:
            board_full.append(i)
        else:
            return False
    if len(board_full) == 8:
        display_board(board)
        announce_tie()
        return True


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