# -*- coding: utf-8 -*-
"""
Created on Sun Feb 26 11:34:07 2017

@author: zcao
"""
"""
Tic-tac-toe (or noughts and crosses) is a simple strategy game in which two players take turns placing a mark on a 3x3 board, attempting to make a row, column, or diagonal of three with their mark. In this homework, we will use the tools we've covered in the past two weeks to create a tic-tac-toe simulator and evaluate basic winning strategies.
"""

import random
import numpy as np
import time
import matplotlib.pyplot as plt


def create_board():
    return np.zeros((3,3))

def place(board, player, position):
    board[position[0],position[1]] = player
         
def possibilities(board):
    return np.transpose(np.where(board == 0))

def random_place(board,player):
    if len(possibilities(board)>0):
        position = random.choice(possibilities(board))
        return place(board,player,position)

def row_win(board,player):
    return np.any((np.all(board[0,:]==player),np.all(board[1,:]==player),np.all(board[2,:]==player))) 

def col_win(board,player):
    return np.any((np.all(board[:,0]==player),np.all(board[:,1]==player),np.all(board[:,2]==player)))

def diag_win(board,player):
    return np.any([np.all([board[i,i]==player for i in range(3)]),np.all([board[i,2-i]==player for i in range(3)])])

def evaluate(board):
    winner = 0
    for player in [1, 2]:
        # Check if `row_win`, `col_win`, or `diag_win` apply.  if so, store `player` as `winner`.
        if(np.any([row_win(board,player),col_win(board,player),diag_win(board,player)])):
            return player
    if np.all(board != 0) and winner == 0:
        winner = -1
    return winner

def play_game():
    board = create_board()
    while np.any(board == 0):
        random_place(board,1)
        random_place(board,2)
    #print(board)
    return evaluate(board)
    
def play_strategic_game():
    board, winner = create_board(), 0
    board[1,1] = 1
    while winner == 0:
        for player in [2,1]:
            # use `random_place` to play a game, and store as `board`.
            random_place(board,player)
            # use `evaluate(board)`, and store as `winner`.
            winner = evaluate(board)
            if winner != 0:
                break
    return winner    
    



st =  time.time()
outs1 = []
for i in range(1000):
    outs1.append(play_game())

ed = time.time()
print(ed-st)
plt.hist(outs1)
plt.show()




st = time.time()
outs2 = []
for i in range(1000):
    outs2.append(play_strategic_game())

ed = time.time()

print(ed-st)

plt.hist(outs2)
plt.show()








