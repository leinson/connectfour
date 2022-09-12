import numpy as np


def create_the_board():
    rows = 7
    columns = 6

    return np.zeros((rows,columns))

def check_if_win():
    pass

def whose_turn():
    pass

def choose_column(column, matrix):
    for i in matrix.T[column]:
      print(i)

#Loop joka aloittaa alimmasta rivistä oikean sarakkeen kohdalta.
#  if x=0: x=playerx. 
# elif laskuri=sarake käyty läpi, return false. 
# muuten jatkaa loop kunnes löytää paikan if lauseesta.

player1 = 1
player2 = 2



board = create_the_board()

choose_column(int(input("Valitse sarake 0-6: ")), board)
