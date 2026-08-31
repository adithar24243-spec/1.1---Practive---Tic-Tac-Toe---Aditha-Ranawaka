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
            board.append = []
    return board 

def display_board(board):
    row_numbers = " "
    for j in range(3):
        row_numbers = row_numbers + " " + str(j+1) + ""

    print("        " + row_numbers)

    row_string = ""

    for j in range(3):
        row_string = row_string + "[" + board[i][j] + "]"

    if(i == 1):
        print("[column]" + str(i) " " + (row_string))
    else:
        print("        " + str(i) + " " + (row_string))


#--------------------------main routine------------------------

create_board()