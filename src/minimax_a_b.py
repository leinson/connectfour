import functions


def heuristic_value(board, chip):
    """Laskee pisteet terminal nodeissa.
    Args:
        board (array): pelilauta
        chip (int): pelinappula
    Returns:
        int: palauttaa kyseisen pelitilanteen pisteet
    """
    value = 0
    columns = 7
    rows = 6
    others_chip = 1

    # 4-rivissä
    for col in range(columns-3):
        for row in range(rows):
            if board[row][col] == chip and board[row][col+1] == chip and board[row][col+2] == chip and board[row][col+3] == chip:
                value += 200
    for col in range(columns):
        for row in range(rows-3):
            if board[row][col] == chip and board[row+1][col] == chip and board[row+2][col] == chip and board[row+3][col] == chip:
                value += 200
    for col in range(columns-3):
        for row in range(3, rows):
            if board[row][col] == chip and board[row-1][col+1] == chip and board[row-2][col+2] == chip and board[row-3][col+3] == chip:
                value += 200
    for col in range(columns-3):
        for row in range(rows-3):
            if board[row][col] == chip and board[row+1][col+1] == chip and board[row+2][col+2] == chip and board[row+3][col+3] == chip:
                value += 200

    # vastustajan 4-rivissä
    for col in range(columns-3):
        for row in range(rows):
            if board[row][col] == others_chip and board[row][col+1] == others_chip and board[row][col+2] == others_chip and board[row][col+3] == others_chip:
                value -= 100
    for col in range(columns):
        for row in range(rows-3):
            if board[row][col] == others_chip and board[row+1][col] == others_chip and board[row+2][col] == others_chip and board[row+3][col] == others_chip:
                value -= 100
    for col in range(columns-3):
        for row in range(3, rows):
            if board[row][col] == others_chip and board[row-1][col+1] == others_chip and board[row-2][col+2] == others_chip and board[row-3][col+3] == others_chip:
                value -= 100
    for col in range(columns-3):
        for row in range(rows-3):
            if board[row][col] == others_chip and board[row+1][col+1] == others_chip and board[row+2][col+2] == others_chip and board[row+3][col+3] == others_chip:
                value -= 100

    #print("value", value)
    return value


def check_if_terminal_node(board):
    """
    Tarkistaa, onko kyseessä lopputapaus tai onko voittoa.
    Args:
        board (array): pelilauta
    Returns:
        boolean: onko lopputapaus / ei enää siirtomahdollisuuksia vai ei
    """
    if functions.get_possible_columns(board) == []:
        return -1
    if functions.check_if_win(board, 1, (-1, -1)) is True:
        return 2
    if functions.check_if_win(board, 0, (-1, -1)) is True:
        return 1
    return False


def minimax(board, depth, alpha, beta, maxplayer):
    """
    Minimax + alpha-beta toteutus wikipedian pseudokoodin mukaan.
        Args:
        board (array): pelilauta
        depth (int): syvyys
        maxplayer (boolean): maksimoija vai minimoija
    Returns:
        tuple: sarake sekä minimax-arvo
    """
    possible_columns = functions.get_possible_columns(board)
    terminal_node = check_if_terminal_node(board)

    chip = 2
    # siirrä näitä terminal node funktioon, siistimpi
    if terminal_node == 2:
        if depth == 5:
            return None, 3000  # kokeilu, jotta suosii matalan syvyyksien voittoja
        return None, 2000
    if terminal_node == 1:
        if depth == 5:
            return None, -3000
        return None, -2000
    if terminal_node == -1:
        # vaihda tämä tarkistus siirtolaskuriksi kts.alla?
        return None, 0
    if depth == 0:
        return (None, heuristic_value(board, chip))

    if maxplayer:
        # siirtolaskuri joka laskee siirrot 6x7, tarkistus alussa,
        # jotta voi poistaa turhat get possible columns funktiokutsut?
        value = -1000000000000
        for move in possible_columns:
            copy_of_board = board.copy()
            empty_row = functions.next_empty_row(copy_of_board, move)
            copy_of_board[empty_row][move] = 2
            minimax_value = minimax(copy_of_board, depth-1, alpha, beta, False)
            if minimax_value[1] > value:
                value = minimax_value[1]
                column = move
            if value >= beta:
                break
            alpha = max(alpha, value)
            #print("copyboard", copy_of_board)
        print("column:", column, "minimax_value:", minimax_value)
        return column, value

    else:  # miniplayer
        value = +10000000000000
        for move in possible_columns:
            copy_of_board = board.copy()
            empty_row = functions.next_empty_row(copy_of_board, move)
            copy_of_board[empty_row][move] = 1
            minimax_value = minimax(copy_of_board, depth-1, alpha, beta, True)
            if value > minimax_value[1]:
                value = minimax_value[1]
                column = move
            if value <= alpha:
                break
            beta = min(beta, value)
            #print("copyboard", copy_of_board)
        print("column:", column, "minimax_value:", minimax_value)
        return column, value
