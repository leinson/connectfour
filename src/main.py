import numpy as np
from random import randint

#TODO:
"""
    - check_if_win: funktio joka tarkistaa taulukon siirron jälkeen - löytyykö voittoa
        - rivi DONE
        - kolumni DONE
        - diagonaali vasenoikea
        - diagonaali oikeavasen
        - voittotarkistus myös pelaajan jälkeen
    - yksikkötestaus tärkeille funktioille ja ominaisuuksille
    - coverage testikattavuusraportti
    - pylint laaduntarkistus

    - pygame visuaalinen toteutus
    - huomioi virhesyötöt
    - tekoälyn eli minimax + alpha-beta karsinnan työstäminen
    - 

"""

def create_the_board():
    """ Luo pelilaudan, eli nollilla alustettu "matriksi".
    Returns:
        np.zeros: nollilla alustettu numpy taulukko. 
    """
    rows = 6
    columns = 7

    return np.zeros((rows,columns))

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
            print(matrix)
            return (row_counter, column)
        row_counter -= 1
    return False

def ai_choose_column(matrix):
    """ Ei vielä tekoälyä. Kokeilen ensin random-valinnalla, että saan muut pelin toiminnallisuudet pyörimään.
        Valitsee random sarakkeen. Muuten toiminta sama kuin pelaajan funktiossa "choose_column".
    Args:
        matrix (np array): pelilauta
    Returns:
        boolean: True jos sarakkeessa tilaa, False jos sarake täynnä.
    """
    column= randint(0,5)
    row_counter = 5
    for i in reversed(matrix.T[column]):
        if i == 0:
            matrix[row_counter][column] = 2
            print(matrix)
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
    print("row:", row)
    col = row_column[1]
    print("column:", col)
    if turn == 0:
        chip = 1
    else:
        chip = 2
    
    """_summary_

    Returns:
        _type_: _description_
    """
    counter=0
    for i in matrix[row]:
        if i == chip:
            counter+=1
        else:
            counter=0
    if counter >= 4:
        return True
    
    #sarake
    counter=0
    for i in matrix.T[col]:
        if i == chip:
            counter+=1
        else:
            counter=0
    if counter >= 4:
        return True


    return False

    #yritin pohtia eri tapoja toteuttaa tämä. Lauta ei ole erityisen suuri, joten kaikki mahdolliset kombot voisi käydä läpi
    #ilman liian suurta hidastetta. Toisaalta haluisin jättää itse tekoälyalgoritmille mieluummin aikaa kuin voitontarkistukselle.
    #Googlasin tämän pohdintaan liittyen, ja taidankin yrittää tehdä sellaisen, joka tarkistaa voitot viimeisen nappulan sijainnin
    #perusteella. Jos sen tekemiseen kuluu itselleni liikaa aikaa, vaihdan koko laudan läpikäymiseen.

def change_turn(turn):
    """ Vaihtaa vuoron pelaajan ja tekoälyn välillä parillisuuden perusteella.
    Args:
        turn (int): pariton tai parillinen riippuen siitä, kumman vuoro on ollut.
    """
    turn +=1
    turn = turn % 2
    return turn

player = 0
ai_player = 1
turn = player
board = create_the_board()


while True:
    """ Alkuvaiheen pelisilmukka.
        Vuoron omaava valitsee sarakkeen, jos on täynnä, valitsee uudelleen. Pelaaja voi päättää, jos jatketaan tai päätetään peli.
        Vuoronvaihto pelaajan ja tekoälyn välillä.
    """
    print("Pelaaja = 1, tekoäly = 2")
    print("kenenvuoro:", turn)
    if turn == player:
        while True:
            insert_chip = choose_column(int(input("Valitse sarake 0-6: ")), board)
            if insert_chip == False:
                print("sarake täynnä, valitse toinen sarake.")
            else:
                break

        
    elif turn == ai_player:
        """Ei vielä tekoälyä, random valinta.
        """
        print("tekoäly tekee siirron:")
        while True:
            insert_chip = ai_choose_column(board)
            if insert_chip == False:
                print("sarake täynnä, tkoäly valitsee toisen sarakkeen.")
            else:
                break
    else:
        print("virhe vuoronvalinnassa")
        break  

    is_win = check_if_win(board, turn, insert_chip)
    if is_win == True:
        print("voitto!", turn)
        break


    end_or_continue = input("jatka: enter, lopeta: x: ")
    if end_or_continue == "x":
        break

    turn = change_turn(turn)

    


#viikkoraporttiin: onko tässä järkevää käyttää enemmän olio- ja luokkaohjelmointia? 
# Vai onko käytön kannalta se turhaa tai hidastavaa tämän kurssin projektille. 
# Nyt olen vain tehnyt erinäisiä funktioita/metodeja joita kutsutaan.