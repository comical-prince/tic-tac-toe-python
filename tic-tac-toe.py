def check_diagonals(board):
    if board[0][0] == board[1][1] == board[2][2] != "-":
        return board[0][0]
    elif board[0][2] == board[1][1] == board[2][0] != "-":
        return board[0][2]
    else:
        return None
    
def check_row(board):
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != "-":
            return board[i][0] 
    else :
        return None
    
def check_colm(board):
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != "-":
            return board[0][i] 
    else :
        return None
    
def check_winner(board):
    winner = check_row(board)
    if winner != None:
        return winner
    
    winner = check_colm(board)
    if winner != None:
        return winner 
    
    winner = check_diagonals(board)
    if winner != None:
        return winner 
    
    return None


def switch_player(current_player):
    if current_player == "X":
        return "O"
    else :
        return "X"
    

def print_board(board):
    print()
    for row in board:
        print(" | ".join(row))
    print()


def is_board_full(board):
    for row in board:
        if "-" in row:
            return False
    return True


board = [["-","-","-"],["-","-","-"],["-","-","-"]]
current_player = "X"
while True:
    print_board(board)

    try:
        row = int(input(f"Player {current_player}, enter row (0-2): "))
        col = int(input(f"Player {current_player}, enter column (0-2): "))
    except ValueError:
        print("Please enter valid numbers.")
        continue

    if row not in range(3) or col not in range(3):
        print("Invalid position! Choose between 0 and 2.")
        continue

    if board[row][col] != "-":
        print("Cell already taken! Try again.")
        continue

    board[row][col] = current_player

    winner = check_winner(board)
    if winner:
        print_board(board)
        print(f"🎉 Player {winner} wins!")
        break

    if is_board_full(board):
        print_board(board)
        print("🤝 It's a draw!")
        break

    current_player = switch_player(current_player)
    