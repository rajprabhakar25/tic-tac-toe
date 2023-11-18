board = {"top-l": " ", "top-m": " ", "top-r": " ",
         "mid-l": " ", "mid-m": " ", "mid-r": " ",
         "low-l": " ", "low-m": " ", "low-r": " "}

def the_board(board):
    print(board["top-l"] + "|" + board["top-m"] + "|" + board["top-r"])
    print("-+-+-")
    print(board["mid-l"] + "|" + board["mid-m"] + "|" + board["mid-r"])
    print("-+-+-")
    print(board["low-l"] + "|" + board["low-m"] + "|" + board["low-r"])

def play(board):
    turn = "X"
    for i in range(9):
        the_board(board)
        print("Turn for ", turn, ". move on which space? ")
        move = input()
        board[move] = turn

        if board["top-l"] == board["top-m"] == board["top-r"] != " ":
            print(board["top-l"], " Wins")
            break
        elif board["mid-l"] == board["mid-m"] == board["mid-r"] != " ":
            print(board["mid-l"], " Wins")
            break
        elif board["low-l"] == board["low-m"] == board["low-r"] != " ":
            print(board["low-l"], " Wins")
            break
        elif board["top-l"] == board["mid-m"] == board["low-r"] != " ":
            print(board["top-l"], " Wins")
            break
        elif board["low-l"] == board["mid-m"] == board["top-r"] != " ":
            print(board["low-l"], " Wins")
            break
        else:
            pass

        if i == 8:
            print("It's a Tie!!")

        if turn == "X":
            turn = "O"
        else:
            turn = "X"
    return 0

play(board)
the_board(board)
answer = input("Play Again? yes/no")
answer = answer.lower()

if answer == "yes":
    board = {"top-l": " ", "top-m": " ", "top-r": " ",
             "mid-l": " ", "mid-m": " ", "mid-r": " ",
             "low-l": " ", "low-m": " ", "low-r": " "}
    play(board)
else:
    print("Thank you for playing!!")
