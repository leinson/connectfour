
import functions

# Muutamien tärkeiden muuttujien alustus
player = 0
ai_player = 1
turn = player
board = functions.create_the_board()

while True:
    """ Alkuvaiheen pelisilmukka.
        Vuoron omaava valitsee sarakkeen, jos on täynnä, valitsee uudelleen.
        Pelaaja voi päättää, jos jatketaan tai päätetään peli.
        Vuoronvaihto pelaajan ja tekoälyn välillä.
    """

    print("Pelaaja = 1, tekoäly = 2")
    print("kenenvuoro:", turn)
    if turn == player:
        while True:
            insert_chip = functions.choose_column(
                int(input("Valitse sarake 0-6: ")), board)
            if insert_chip is False:
                print("sarake täynnä, valitse toinen sarake.")
            else:
                break
        is_win = functions.check_if_win(board, turn, insert_chip)
        print("Pelilauta \n",board)
        print("row:", insert_chip[0], "\ncolumn:", insert_chip[1])

    elif turn == ai_player:
        """Ei vielä tekoälyä, random valinta.
        """
        print("tekoäly tekee siirron:")
        (column, minimax_value) = functions.minimax(board, 5, -100000000000, +100000000000, True)
        column = int(column)
        if board[0][column] == 0:
            row = functions.next_empty_row(board, column)
            board[row][column] = 2
            is_win = functions.check_if_win(board, turn, (row, column))
        else:
            if functions.get_possible_columns(board) == []:
                print("lauta täynnä, tasapeli")
                break
        print("Pelilauta \n",board)
        print("row:", row, "\ncolumn:", column)
        while False: #random valinta ai
            insert_chip = functions.ai_choose_column(board)
            if insert_chip is False:
                print("sarake täynnä, tkoäly valitsee toisen sarakkeen.")
            else:
                break
  

    if is_win is True:
        print("voitto!", turn)
        break

    end_or_continue = input("jatka: enter, lopeta: x: ")
    if end_or_continue == "x":
        break

    turn = functions.change_turn(turn)
