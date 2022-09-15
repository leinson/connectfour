import numpy as np


def create_the_board():
    """Luo pelilaudan, eli nollilla alustettu "matriksi".

    Returns:
        np.zeros: nollilla alustettu numpy taulukko. 
    """
    rows = 6
    columns = 7

    return np.zeros((rows,columns))

def check_if_win():
    pass

def whose_turn():
    pass

def choose_column(column, matrix):
    """Tarkastaa valittua saraketta alhaalta ylös, onko sarakkeessa vielä tilaa.
    Jos on, sijoitetaan pelinappula siihen kohtaan.

    Args:
        column (int): Sarake, jonka pelaaja on valinnut
        matrix (np array): pelilauta

    Returns:
        boolean: True jos sarakkeessa tilaa, False jos sarake täynnä.
    """
    row_counter=5
    for i in reversed(matrix.T[column]):
        print(i)
        if i==0:
            matrix[row_counter][column]=1
            print(matrix)
            return True
        row_counter-=1
    return False

# seuraavaksi vuoronvaihto toteutus: 

player1 = 1
player2 = 2



board = create_the_board()

while True:
    """Alkuvaiheen pelisilmukka. Valitaan sarake, jatketaan tai päätetään peli.
    """
    
    insert_chip = choose_column(int(input("Valitse sarake 0-6: ")), board)
    if insert_chip == False:
        print("sarake täynnä, valitse toinen sarake.")
    end_or_continue = input("jatka: enter, lopeta: n: ")
    if end_or_continue == "n":
        break
