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


def ai_choose_column(matrix):
    """ Ei vielä tekoälyä. Kokeilen ensin random-valinnalla,
        että saan muut pelin toiminnallisuudet pyörimään.
        Valitsee random sarakkeen. Muuten toiminta sama kuin
        pelaajan funktiossa "choose_column".
    Args:
        matrix (np array): pelilauta
    Returns:
        boolean: True jos sarakkeessa tilaa, False jos sarake täynnä.
    """
    column = randint(0, 5)
    row_counter = 5
    for i in reversed(matrix.T[column]):
        if i == 0:
            matrix[row_counter][column] = 2
            return (row_counter, column)
        row_counter -= 1
    return False


def check_if_win(matrix, turn, row_column):
    """ Tarkistetaan, onko voittoriviä. Valitaan, kenen nappuloita katsotaan.
    Args:
        matrix (array): pelilauta
        turn (int): kenen vuoro (0 tai 1)
    Returns:
        boolean: True jos voitto löytynyt, muuten False
    """
    if turn == 0:
        chip = 1
    else:
        chip = 2
    rows = 6
    columns = 7

    #pidempi silmukka jos käydään minimax algoritmia, jolloin tarkka paikka
    #ei ole tiedossa
    if row_column == (-1,-1):
        #rivi
        for i in range(columns-3):
            for j in range(rows):
                if matrix[j][i] == chip and matrix[j][i+1] == chip and matrix[j][i+2] == chip and matrix[j][i+3] == chip:
                    return True
        #sarake
        for i in range(columns):
            for j in range(rows-3):
                if matrix[j][i] == chip and matrix[j+1][i] == chip and matrix[j+2][i] == chip and matrix[j+3][i] == chip:
                    return True

    else:    
        row = row_column[0]
        col = row_column[1]
        
        # rivi
        counter = 0
        for i in matrix[row]:
            if i == chip:
                counter += 1
            else:
                counter = 0
            print("rivicounter:", counter)
            if counter >= 4:
                return True

        # sarake
        counter = 0
        for i in matrix.T[col]:
            if i == chip:
                counter += 1
            else:
                counter = 0
            print("sarakecounter:", counter)
            if counter >= 4:
                return True

    # diagonaalit, Käy kaikki vaihtoehdot läpi paitsi ne, mihin ei
    # voi tulla voittoa. 

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
    """ Vaihtaa vuoron pelaajan ja tekoälyn välillä parillisuuden perusteella.
    Args:
        turn (int): pariton tai parillinen riippuen siitä, kumman vuoro on ollut.
    """
    turn += 1
    turn = turn % 2
    return turn

def get_possible_columns(board):
    """Tarkistaa ylimmän rivin, minkä sarakkeiden kohdalla on vielä tyhjää.
    Args:
        board (array): pelilauta
    Returns:
        list: listan mahdollisista sarakkeista.
    """
    possible_columns = []
    columns = 7
    last_row = 0
    for column in range(columns):
        if board[last_row][column] == 0:
            possible_columns.append(column)
    #print("get possible columns:", possible_columns)
    return possible_columns

def check_if_terminal_node(board):
    """
    Onko kyseessä lopputapaus, Onko mahdollisia siirtoja jäljellä.
    Tarkistetaan onko voittoa todettavissa pelaajalla tai ai:lla. 
    Args:
        board (array): pelilauta
    Returns:
        boolean: onko lopputapaus vai ei
    """
    if len(get_possible_columns(board)) == 0:
        return True
    elif check_if_win(board, 0, (-1,-1)) is True or check_if_win(board, 0, (-1,-1)) is True:
        return True
    return False

def heuristic_value(board, chip):
    """Pisteet siirrosta:
    4-connect = 1000
    3-connect = 10
    2-connect = 5
    3-connect vastustaja = -5

    Args:
        board (_type_): _description_
        chip (_type_): _description_
    """
    value = 0
    #horisontaalinen 4-rivissä
    columns=7
    rows=6
    for col in range(columns-3):
        for row in range(rows):
            if board[row][col] == chip and board[row][col+1] == chip and board[row][col+2] == chip:
                    value += 10000
                    print("value", value)
                    
    for col in range(columns-3):
        for row in range(rows):
            if board[row][col] == 1 and board[row][col+1] == 1 and board[row][col+2] == 1:
                    value -= 10000
                    print("value vastustaja", value)
    return value

def next_empty_row(board, column):
    for row in range(5,-1,-1):
        if board[row][column] == 0:
            return row


b=create_the_board()
b[5][0]=1
b[5][1]=1
b[5][2]=1
b[5][3]=1
print(heuristic_value(b, 1))
print(check_if_win(b, 0, (-1,-1)))
print(b)
print(next_empty_row(b, 5))

def minimax(board, depth, maxplayer):
    """
    Minimax toteutus wikipedian pseudokoodin mukaan.
    Lisäksi katsottu erilaisia toteutuksia algoritmista pelien koodeissa.
    Ei vielä Alpha-beta-karsintaa. 

    Args:
        board (array): pelilauta
        depth (int): syvyys
        maxplayer (boolean): maksimoija vai minimoija

    Returns:
        tuple: sarake sekä minimax-arvo
    """

    possible_columns = get_possible_columns(board)
    terminal_node = check_if_terminal_node(board)

    if depth == 0 or terminal_node is True: 
        if terminal_node is True:
            if check_if_win(board, 1, (-1,-1)):
                return (None, -9999999999999)
            elif check_if_win(board, 2, (-1,-1)):
                return (None, 99999999999999)
        else: #syvyys = 0
            return None, heuristic_value(board, 2)

    if maxplayer:
        value = -1000000000000 #vaihda oikea infinity?
        for move in possible_columns:
            copy_of_board = board.copy()
            empty_row = next_empty_row(copy_of_board, move)
            copy_of_board[empty_row][move] == 2
            #value = max(value, minimax(copy_of_board, depth-1, False))
            minimax_value = minimax(copy_of_board, depth-1, False)
            value = max(value, minimax_value[1])
        return move, value

    else: #miniplayer
        value= +10000000000000
        for move in possible_columns:
            copy_of_board = board.copy()
            empty_row = next_empty_row(copy_of_board, move)
            copy_of_board[empty_row][move] == 1
            #value = min(value, minimax(copy_of_board, depth-1, True))
            minimax_value = minimax(copy_of_board, depth-1, True)
            value = min(value, minimax_value[1])
        return move, value

    #    for each child of node do
    #        value := max( value, minimax( child, depth − 1, FALSE ) )
    #    return value

    #else (* minimizing player *)
    #    value := +∞
    #    for each child of node do
    #        value := min( value, minimax( child, depth − 1, TRUE ) )
    #    return value