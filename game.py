board = ["  " for i in range(9)]

def print_board():
    row_1 = "| {} | {} | {} |".format(board[0],board[1],board[2])
    row_2 = "| {} | {} | {} |".format(board[3],board[4],board[5])
    row_3 = "| {} | {} | {} |".format(board[6],board[7],board[8])

    print()
    print(row_1)
    print(row_2)
    print(row_3)
    print()

def player_move(icon):
    if icon == "x":
        number = 1
    elif icon == "o":
        number = 2   
    print("Your turn player {}".format(number))
    
    choice  =  int(input("Enter you move (1-9): ").strip())
    if board[choice - 1]  == "  ":
        board[choice - 1] =  icon
    else:
        print("This space is taken! Please try another")
        player_move(icon)

def is_victory(icon):
    if (board[0] ==  icon and board[1] == icon and board[2] == icon) or \
       (board[3] ==  icon and board[4] == icon and board[5] == icon) or \
       (board[6] ==  icon and board[7] == icon and board[8] == icon) or \
       (board[0] ==  icon and board[4] == icon and board[8] == icon) or \
       (board[2] ==  icon and board[4] == icon and board[6] == icon) or \
       (board[0] ==  icon and board[3] == icon and board[6] == icon) or \
       (board[1] ==  icon and board[4] == icon and board[7] == icon) or \
       (board[2] ==  icon and board[5] == icon and board[8] == icon) :
            return True
    else:
            return False

def is_draw():
    if "  " not in board:
        return True
    else:
        return False
    
while True:
    print_board()
    player_move("x")
    print_board()
    
    if is_victory("x"):
        print_board()
        print("X Wins! Congratulations!")
        break
    elif is_draw():
        print("It's a Draw!")
        break
    player_move("o")
    if is_victory("o"):
        print_board()
        print("O  Wins! Congratulations!")
        break
    elif is_draw():
        print("It's a Draw!")
        break


















