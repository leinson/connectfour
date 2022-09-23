import pygame
import numpy as np
import functions

# TODO:
    # neliöiden sijaan circles
    # näytölle myös ohjeet ja kommentit jotka atm terminaaliin
    # Taulukon ulkopuolelle klikkaamisen virheen korjaus

def ui_pygame():   
    """ Pygame graafinen käyttöjärjestelmä. 
        Oikean sarakkeen painaminen tiputtaa nappulan kyseiseen sarakkeeseen.
        Voitto tulostuu tällä hetkellä terminaaliin.
        Pelilaudan rakentamiseen otettu inspiraatiota ja ohjeita seuraavista lähteistä:
        https://dr0id.bitbucket.io/legacy/pygame_tutorial00.html
        https://pygame.readthedocs.io/en/latest/1_intro/intro.html
    """
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREY = (127, 127, 127)

    WIDTH = 80
    HEIGHT = 80
    MARGIN = 20

    board = functions.create_the_board()
    board = np.zeros((6, 7)) 
    board[1][4] = 1
    board[3][2] = 2

    pygame.init()

    WINDOW_SIZE = [720, 650]
    screen = pygame.display.set_mode(WINDOW_SIZE)
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

            elif event.type == pygame.MOUSEBUTTONDOWN and turn == player and game_over == False:
                position = pygame.mouse.get_pos()
                column = position[0] // (WIDTH + MARGIN)
                row = position[1] // (HEIGHT + MARGIN)
    
                insert_chip = functions.choose_column(column, board)
                #print(insert_chip)
                #print(position, "koordinaatit:", row, column)
                if insert_chip is False:
                    print("Sarake täynnä, valitse toinen sarake.")
                else:
                    is_win = functions.check_if_win(board, turn, insert_chip)
                    turn = functions.change_turn(turn)
                    if is_win is True:
                            print("Sinä voitit!")
                            game_over = True
                    
        
        if turn == ai_player and game_over == False:
            insert_ai_chip = functions.ai_choose_column(board)
            if insert_ai_chip is False:
                print("AIn valitsema sarake on täynnä, valitsee toisen")
            else:
                is_win = functions.check_if_win(board, turn, insert_ai_chip)
                turn = functions.change_turn(turn)
                if is_win is True:
                        print("AI voitti!")
                        game_over = True   
        screen.fill(GREY)
# pelilaudan piirto
        for row in range(6):
            for column in range(7):
                color = WHITE
                if board[row][column] == 1:
                    color = BLUE
                elif board[row][column] == 2:
                    color = RED
                pygame.draw.rect(screen,
                                color,
                                [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH,
                                HEIGHT])
        pygame.display.update()
    pygame.quit()

ui_pygame()