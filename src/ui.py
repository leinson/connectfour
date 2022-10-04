
import pygame
import numpy as np
import functions

# TODO:
# minimaxin yhdistäminen tähän
# neliöiden sijaan circles
# näytölle myös ohjeet ja kommentit jotka atm terminaaliin
# Taulukon ulkopuolelle klikkaamisen virheen korjaus


def ui_pygame():
    """ Pygame graafinen käyttöjärjestelmä ILMAN MINIMAXIA.
        Oikean sarakkeen painaminen tiputtaa nappulan kyseiseen sarakkeeseen.
        Voitto tulostuu tällä hetkellä terminaaliin.
        Pelilaudan rakentamiseen otettu inspiraatiota ja ohjeita seuraavista lähteistä:
        https://dr0id.bitbucket.io/legacy/pygame_tutorial00.html
        https://pygame.readthedocs.io/en/latest/1_intro/intro.html
    """
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    grey = (127, 127, 127)

    width = 80
    height = 80
    margin = 20

    board = functions.create_the_board()

    pygame.init()

    window_size = [720, 650]
    screen = pygame.display.set_mode(window_size)
    pygame.display.set_caption("ConnectFour")
    done = False

    player = 0
    ai_player = 1
    turn = player
    game_over = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            
            if game_over is False and functions.get_possible_columns(board) == []:
                print("pelilauta täynnä, tasapeli!")
                game_over = True

            elif event.type == pygame.MOUSEBUTTONDOWN and turn == player and game_over is False:
                position = pygame.mouse.get_pos()
                column = position[0] // (width + margin)
                row = position[1] // (height + margin)

                insert_chip = functions.choose_column(column, board)
                if insert_chip is False:
                    print("Sarake täynnä, valitse toinen sarake.")
                else:
                    is_win = functions.check_if_win(board, turn, insert_chip)
                    if is_win is True:
                        print("Sinä voitit!")
                        game_over = True
                    turn = functions.change_turn(turn)

        if turn == ai_player and game_over is False:
            insert_ai_chip = functions.ai_choose_column(board)
            if insert_ai_chip is False:
                print("AIn valitsema sarake on täynnä, valitsee toisen")
            else:
                is_win = functions.check_if_win(board, turn, insert_ai_chip)
                turn = functions.change_turn(turn)
                if is_win is True:
                    print("AI voitti!")
                    game_over = True
        screen.fill(grey)
# pelilaudan piirto
        for row in range(6):
            for column in range(7):
                color = white
                if board[row][column] == 1:
                    color = blue
                elif board[row][column] == 2:
                    color = red
                pygame.draw.rect(screen,
                                 color,
                                 [(margin + width) * column + margin,
                                  (margin + height) * row + margin,
                                  width,
                                  height])
        pygame.display.update()
    pygame.quit()


ui_pygame()
