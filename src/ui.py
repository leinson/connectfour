
import pygame
import functions
import minimax_a_b


def draw_board(board, screen, margin, width, height, text):
    font = pygame.font.SysFont("monospace", 35, True)
    white = (255, 255, 255)
    red = (255, 0, 0)
    blue = (0, 0, 255)
    grey = (127, 127, 127)
    screen.fill(grey)
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
                                 height]
                             )

    label = font.render(text, 1, blue)
    screen.blit(label, (30, 620))

    pygame.display.update()


def ui_pygame(screen):
    """ Pygame graafinen käyttöjärjestelmä, ai aloittaa.
        Oikean sarakkeen painaminen tiputtaa nappulan kyseiseen sarakkeeseen.
        Voitto tulostuu tällä hetkellä terminaaliin.
    """
    board = functions.create_the_board()
    done = False
    width = 80
    height = 80
    margin = 20
    player = 0
    ai_player = 1
    turn = ai_player
    game_over = False
    turn_counter = 0
    text = ""
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.MOUSEBUTTONDOWN and turn == player and game_over is False:
                position = pygame.mouse.get_pos()
                column = position[0] // (width + margin)
                row = position[1] // (height + margin)
                if column == 7:
                    column = 6

                insert_chip = functions.choose_column(column, board)
                if insert_chip is False:
                    text = "Täynnä, valitse toinen sarake."
                else:
                    is_win = functions.check_if_win(board, turn, insert_chip)
                    if is_win is True:
                        text = "Sinä voitit!"
                        game_over = True
                    text = ""
                    turn = functions.change_turn(turn)

                    turn_counter += 1
                    if turn_counter == 21 and is_win is False:
                        game_over = True
                        text = "Tasapeli"

                draw_board(board, screen, margin, width, height, text)

        if turn == ai_player and game_over is False:
            column, minimax_value = minimax_a_b.minimax(
                board, 6, -100000000000, +100000000000, True)
            if board[0][column] == 0:
                row = functions.next_empty_row(board, column)
                board[row][column] = 2
                is_win = functions.check_if_win(board, turn, (row, column))
                if is_win is True:
                    text = "AI voitti!"
                    game_over = True
            else:
                text = "Tasapeli"
                game_over = True
            turn = functions.change_turn(turn)

            draw_board(board, screen, margin, width, height, text)

    pygame.quit()
