from turtle import position
import pygame
import numpy as np

# pelilaudan rakentamiseen otettu inspiraatiota seuraavista lähteistä:
# https://dr0id.bitbucket.io/legacy/pygame_tutorial00.html
# https://pygame.readthedocs.io/en/latest/1_intro/intro.html

def ui_pygame():   
    """ Pygame graafinen käyttöjärjestelmä-runko. 
        Ei vielä yhdistetty oikeaan pelilogiikkaan.
        Luo pelilaudan, sekä mahdollisuuden hiirellä
        valita ruudun. Jatkossa sarakkeen painaminen 
        pitäisi luoda nappulan oikeaan kohtaan sarakkeessa.

    """
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    BLUE = (0, 0, 255)
    GREY = (127, 127, 127)

    WIDTH = 80
    HEIGHT = 80
    MARGIN = 20

    test_board = np.zeros((6, 7)) 
    test_board[1][4] = 1
    test_board[3][2] = 2

    pygame.init()

    WINDOW_SIZE = [720, 650]
    screen = pygame.display.set_mode(WINDOW_SIZE)
    pygame.display.set_caption("ConnectFour")
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                position = pygame.mouse.get_pos()
                column = position[0] // (WIDTH + MARGIN)
                row = position[1] // (HEIGHT + MARGIN)
                test_board[row][column] = 1
                print(position, "koordinaatit:", row, column)
        screen.fill(GREY)
    # pelilaudan piirto
        for row in range(6):
            for column in range(7):
                color = WHITE
                if test_board[row][column] == 1:
                    color = BLUE
                elif test_board[row][column] == 2:
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