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
    board = []

    for i in range(3):
        row = []
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
    board = create_board
    current_player = "X"

    print("Welcome to the Tic Tac Toe game")
    print("Player 1 is X | Player 2 is O")

    while(True):

        display_board(board)

        print("It is player 1's turn")
        col = int(input("Enter a column (0,1,2):"))
        row = int(input("Enter a row (0,1,2):"))

        board[col][row] = current_player

        if(current_player == "X"):
            current_player = "O"
        else:
            current_player = "X"

#--------------------------main routine------------------------

myboard = create_board()
display_board(myboard)
