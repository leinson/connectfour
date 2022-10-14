
import pygame
import functions
import minimax_a_b


def draw_board(board, screen, margin, width, height, text):
    font = pygame.font.Font("src/assets/PlaymegamesReguler-2OOee.ttf", 50)
    empty_slots_color = (229, 204, 255)
    ai_color = (255, 153, 51)
    player_color = (153, 51, 255)
    background = (51, 0, 102)
    text_color = (153, 51, 255)
    screen.fill(background)
    for row in range(6):
        for column in range(7):
            color = empty_slots_color
            if board[row][column] == 1:
                color = player_color
            elif board[row][column] == 2:
                color = ai_color
            pygame.draw.rect(screen,
                             color,
                             [(margin + width) * column + margin,
                                 (margin + height) * row + margin,
                                 width,
                                 height]
                             )

    label = font.render(text, 1, text_color)
    screen.blit(label, (120, 625))

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
    text = "  . : I CONNECT FOUR I : ."
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
                    text = "Valitse toinen sarake."
                else:
                    is_win = functions.check_if_win(board, turn, insert_chip)
                    if is_win is True:
                        text = "OLET VOITTAJA !"
                        game_over = True
                    text = "  . : I CONNECT FOUR I : ."
                    turn = functions.change_turn(turn)

                    turn_counter += 1
                    if turn_counter == 21 and is_win is False:
                        game_over = True
                        text = "Tasapeli - GAME OVER"

                draw_board(board, screen, margin, width, height, text)

        if turn == ai_player and game_over is False:
            column, minimax_value = minimax_a_b.minimax(
                board, 6, -100000000000, +100000000000, True)
            if board[0][column] == 0:
                row = functions.next_empty_row(board, column)
                board[row][column] = 2
                is_win = functions.check_if_win(board, turn, (row, column))
                if is_win is True:
                    text = "AI VOITTI ! GAME OVER"
                    game_over = True
            else:
                text = "Tasapeli - GAME OVER"
                game_over = True
            turn = functions.change_turn(turn)

            draw_board(board, screen, margin, width, height, text)

    pygame.quit()
