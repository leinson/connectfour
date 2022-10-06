from random import randint
import numpy as np


def create_the_board():
    """ Luo pelilaudan, eli nollilla alustettu "matriksi".
    Returns:
        np.zeros: nollilla alustettu numpy taulukko.
    """
    rows = 6
    columns = 7
    return np.zeros((rows, columns))


def choose_column(column, matrix):
    """ Tarkastaa valittua saraketta alhaalta ylös, onko sarakkeessa vielä tilaa.
        Jos on, sijoitetaan pelinappula siihen kohtaan.
    Args:
        column (int): Sarake, jonka pelaaja on valinnut
        matrix (np array): pelilauta
    Returns:
        boolean: True jos sarakkeessa tilaa, False jos sarake täynnä.
    """
    row_counter = 5
    for i in reversed(matrix.T[column]):
        if i == 0:
            matrix[row_counter][column] = 1
            return (row_counter, column)
        row_counter -= 1
    return False


# def ai_choose_column(matrix):
#     """ POISTA kun minimax toimii.
#         Kokeilen ensin random-valinnalla,
#         että saan muut pelin toiminnallisuudet pyörimään.
#         Valitsee random sarakkeen. Muuten toiminta sama kuin
#         pelaajan funktiossa "choose_column".
#     Args:
#         matrix (np array): pelilauta
#     Returns:
#         boolean: True jos sarakkeessa tilaa, False jos sarake täynnä.
#     """
#     column = randint(0, 5)
#     row_counter = 5
#     for i in reversed(matrix.T[column]):
#         if i == 0:
#             matrix[row_counter][column] = 2
#             return (row_counter, column)
#         row_counter -= 1
#     return False


def check_if_win(matrix, turn, row_column):
    """ Tarkistetaan, onko voittoriviä. Valitaan, kenen nappuloita katsotaan.
    Args:
        matrix (array): pelilauta
        turn (int): kenen vuoro (0 tai 1)
        row_column (tuple): valitun nappulan koordinaatit. Jos minimaxin kautta kutsu tähän metodiin, on arvo (-1,-1).
    Returns:
        boolean: True jos voitto löytynyt, muuten False
    """
    if turn == 0:
        chip = 1
    else:
        chip = 2
    rows = 6
    columns = 7
    row = row_column[0]
    col = row_column[1]

    # pidempi silmukka jos käydään minimax algoritmia, jolloin tarkka paikka ei ole tiedossa
    if row_column == (-1, -1):
        # rivi
        for i in range(columns-3):
            for j in range(rows):
                if matrix[j][i] == chip and matrix[j][i+1] == chip and matrix[j][i+2] == chip and matrix[j][i+3] == chip:
                    return True
        # sarake
        for i in range(columns):
            for j in range(rows-3):
                if matrix[j][i] == chip and matrix[j+1][i] == chip and matrix[j+2][i] == chip and matrix[j+3][i] == chip:
                    return True
    else:
        # rivi
        counter = 0
        for i in matrix[row]:
            if i == chip:
                counter += 1
            else:
                counter = 0
            if counter >= 4:
                return True
        # sarake
        counter = 0
        for i in matrix.T[col]:
            if i == chip:
                counter += 1
            else:
                counter = 0
            if counter >= 4:
                return True

    # diagonaalit, Käy kaikki vaihtoehdot läpi paitsi ne, mihin ei voi tulla voittoa.
    # /-diagonaali
    for i in range(columns-3):
        for j in range(3, rows):
            if matrix[j][i] == chip:
                if matrix[j-1][i+1] == chip and matrix[j-2][i+2] == chip and matrix[j-3][i+3] == chip:
                    return True
    # \-diagonaali
    for i in range(columns-3):
        for j in range(rows-3):
            if matrix[j][i] == chip:
                if matrix[j+1][i+1] == chip and matrix[j+2][i+2] == chip and matrix[j+3][i+3] == chip:
                    return True
    return False


def change_turn(turn):
    """
    Vaihtaa vuoron pelaajan ja tekoälyn välillä parillisuuden perusteella.
    Args:
        turn (int): pariton tai parillinen riippuen siitä, kumman vuoro on ollut.
    """
    turn += 1
    turn = turn % 2
    return turn


def get_possible_columns(board):
    """
    Tarkistaa ylimmän rivin: minkä sarakkeiden kohdalla on vielä tyhjää, eli 0.
    Args:
        board (array): pelilauta
    Returns:
        list: listan mahdollisista sarakkeista.
    """
    possible_columns = [3, 2, 4, 1, 5, 0, 6]
    columns = 7
    last_row = 0
    for column in range(columns):
        if board[last_row][column] != 0:
            possible_columns.remove(column)
    return possible_columns


def next_empty_row(board, column):
    for row in range(5, -1, -1):
        if board[row][column] == 0:
            return row
