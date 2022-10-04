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
    """ POISTA kun minimax toimii.
        Kokeilen ensin random-valinnalla,
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
    #0123456
    #3241506
    possible_columns = [3, 2, 4, 1, 5, 0, 6]
    #possible_columns = []
    columns = 7
    last_row = 0
    for column in range(columns):
        if board[last_row][column] != 0:
            possible_columns.remove(column)
        # if board[last_row][column] == 0:
        #     possible_columns.append(column)
    return possible_columns


def check_if_terminal_node(board):
    """
    Onko kyseessä lopputapaus, vai onko mahdollisia siirtoja jäljellä.
    Tarkistetaan, onko voittoa todettavissa pelaajalla tai ai:lla.
    Args:
        board (array): pelilauta
    Returns:
        boolean: onko lopputapaus / ei enää siirtomahdollisuuksia vai ei
    """
    if get_possible_columns(board) == []:
        return True
    if check_if_win(board, 0, (-1, -1)) is True:
        return True
    elif check_if_win(board, 1, (-1, -1)) is True:
        return True
    else:
        return False


def heuristic_value(board, chip):
    """Pisteet siirroista :
    4-connect = 200
    4-connect vastustaja = -100
    tasapeli = 50
    Käydään läpi eri vaihtoehdot saada pisteitä ja lasketaan yhteispisteet.
    Blokkaa atm rivi+sarakevoitot hyvin, ei huomaa hyvin omia voittomahiksia. 
    Pisteytykseen liittyen otettu ideaa tästä videosta: https://www.youtube.com/watch?v=y7AKtWGOPAE&t=0s
    Args:
        board (array): pelilauta
        chip (int): pelinappula
    Returns:
        int: palauttaa kyseisen vaihtoehtoisen pelilaudan pisteet
    """
    value = 0
    columns = 7
    rows = 6
    if chip == 2:
        others_chip = 1
    else:
        others_chip = 2
    tie_1 = 0
    tie_2 =0
    # 4-rivissä
    for col in range(columns-3):
        for row in range(rows):
            if board[row][col] == chip and board[row][col+1] == chip and board[row][col+2] == chip and board[row][col+3] == chip:
                value += 200
                tie_1 += 1
    for col in range(columns):
        for row in range(rows-3):
            if board[row][col] == chip and board[row+1][col] == chip and board[row+2][col] == chip and board[row+3][col] == chip:
                value +=200
                tie_1 += 1 
    for col in range(columns-3):
        for row in range(3, rows):
            if board[row][col] == chip and board[row-1][col+1] == chip and board[row-2][col+2] == chip and board[row-3][col+3] == chip:
                value +=200
                tie_1 += 1
    for col in range(columns-3):
        for row in range(rows-3):
            if board[row][col] == chip and board[row+1][col+1] == chip and board[row+2][col+2] == chip and board[row+3][col+3] == chip:
                value+=200
                tie_1 += 1

    # vastustajan 4-rivissä
    for col in range(columns-3):
        for row in range(rows):
            if board[row][col] == others_chip and board[row][col+1] == others_chip and board[row][col+2] == others_chip and board[row][col+3] == others_chip:
                value -= 100
                tie_2 +=1
    for col in range(columns):
        for row in range(rows-3):
            if board[row][col] == others_chip and board[row+1][col] == others_chip and board[row+2][col] == others_chip and board[row+3][col] == others_chip:
                value -=100
                tie_2 +=1
    for col in range(columns-3):
        for row in range(3, rows):
            if board[row][col] == others_chip and board[row-1][col+1] == others_chip and board[row-2][col+2] == others_chip and board[row-3][col+3] == others_chip:
                    value -=100
                    tie_2 +=1                     
    for col in range(columns-3):
        for row in range(rows-3):
            if board[row][col] == others_chip and board[row+1][col+1] == others_chip and board[row+2][col+2] == others_chip and board[row+3][col+3] == others_chip:
                    value-=100
                    tie_2 +=1
    # tasapeli
    if tie_1 != 0 and tie_2 != 0:
        value = 50

    print("value", value)
    return value

def next_empty_row(board, column):
    for row in range(5, -1, -1):
        if board[row][column] == 0:
            return row


def minimax(board, depth, alpha, beta, maxplayer):
    """
    Minimax toteutus wikipedian pseudokoodin mukaan. Lisäksi katsottu erilaisia toteutuksia algoritmista pelien koodeissa.
    Keskeneräinen. Ei vielä Alpha-beta-karsintaa.
    Args:
        board (array): pelilauta
        depth (int): syvyys
        maxplayer (boolean): maksimoija vai minimoija
    Returns:
        tuple: sarake sekä minimax-arvo
    """
    possible_columns = get_possible_columns(board)
    terminal_node = check_if_terminal_node(board)
    print("terminal node", terminal_node)
    if maxplayer is True:
        chip = 2
    else:
        chip = 1
    if terminal_node is True or depth == 0:
        return (None, heuristic_value(board, chip))

    if maxplayer:
        value = -1000000000000 
        for move in possible_columns:
            copy_of_board = board.copy()
            empty_row = next_empty_row(copy_of_board, move)
            copy_of_board[empty_row][move] = 2
            minimax_value = minimax(copy_of_board, depth-1, alpha, beta, False)
            print("minimax_value", minimax_value)
            if minimax_value[1] > value:
                value = minimax_value[1]
                column = move
            if value >= beta:
                break
            alpha = max(alpha, value)
            print("copyboard", copy_of_board)
        return column, value

    else:  # miniplayer
        value = +10000000000000
        for move in possible_columns:
            copy_of_board = board.copy()
            empty_row = next_empty_row(copy_of_board, move)
            copy_of_board[empty_row][move] = 1
            minimax_value = minimax(copy_of_board, depth-1, alpha, beta, True)
            if value > minimax_value[1]:
                value = minimax_value[1]
                column = move
            if value <= alpha:
                break
            beta = min(beta, value)
            print("copyboard", copy_of_board)
        return column, value
