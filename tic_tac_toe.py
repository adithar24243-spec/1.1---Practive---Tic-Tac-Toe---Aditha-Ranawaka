'''
    author: Aditha Mansilu Ranawaka
    date: 26/8/2026
    version: 
    description: Rock, paper, scissor game
''' 

#--------------------------libraries---------------------------
import random

#--------------------------functions---------------------------

def create_board():
    board = [] # create an empty list to store the board

    for i in range(3):
        row = [] # create an empty list to store the rows
        for j in range(3):
            row.append("_")
        board.append(row)
    return board 

def display_board(board):
    row_numbers = " "
    for j in range(3):
        row_numbers = row_numbers + " " + str(j) + ""

    print("            [row]")
    print("          " + row_numbers)

    for i in range(3):
        row_string = ""
        for j in range(3):
            row_string = row_string + "[" + board[i][j] + "]"

        if(i == 1):
            print("[column]" + str(i) + " " + (row_string))
        else:
            print("        " + str(i) + " " + (row_string))

def main():
    board = create_board()
    print("Welcome to the Tic Tac Toe game") # welcome message

    current_player = "X"

    while(True):

        display_board(board)

        print("Player 1 is X | Player 2 is O")

        # this if and esle is responsible for the players' symbol (X or O)
        if(current_player == "X"):
            player_num = 1
        else:
            player_num = 2
        
        print(f"It is player {player_num}'s turn")
        col = int(input("Enter a column (0,1,2):")) # input for the column number
        row = int(input("Enter a row (0,1,2):")) # input for the row number

        if(board[col][row] == "_"):
            board[col][row] = current_player # tracks the location of the coordination input
            valid_move = True

            # this if and else condition switch the player's turn from one to another
            if(current_player == "X"):
                current_player = "O"
            else:
                current_player = "X"

        else:
            print("This place is already taken. Enter another box.")

        
#--------------------------main routine------------------------

if (__name__ == "__main__"):
    main()
