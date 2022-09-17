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
    row = row_column[0]
    col = row_column[1]
    if turn == 0:
        chip = 1
    else:
        chip = 2

    # rivi ei toimi täytyy muokata
    counter = 0
    for i in matrix[row]:
        if i == chip:
            counter += 1
        else:
            counter = 0
    if counter >= 4:
        return True

    # sarake toimii
    counter = 0
    for i in matrix.T[col]:
        if i == chip:
            counter += 1
        else:
            counter = 0
    if counter >= 4:
        return True

    # horisontaaliset tekemättä

    return False


def change_turn(turn):
    """ Vaihtaa vuoron pelaajan ja tekoälyn välillä parillisuuden perusteella.
    Args:
        turn (int): pariton tai parillinen riippuen siitä, kumman vuoro on ollut.
    """
    turn += 1
    turn = turn % 2
    return turn
