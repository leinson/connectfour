import numpy as np
import unittest
import functions
import minimax_a_b


class TestMiniMax(unittest.TestCase):
    """
    Testejä liittyen minimax-funktion toimintaan.
    """
    def setUp(self):
        self.board = functions.create_the_board()

    def test_minimax_wins_in_row(self):
        for i in range(3):
            self.board[5][i] = 2

        column, minimax_value = minimax_a_b.minimax(
            self.board, 6, -10000000000, +100000000000, True)
        self.assertEqual(3, column)

    def test_minimax_wins_in_column(self):
        for i in range(3):
            self.board[i+3][2] = 2

        column, minimax_value = minimax_a_b.minimax(
            self.board, 6, -10000000000, +100000000000, True)
        self.assertEqual(2, column)

    def test_minimax_wins_in_diagonal1(self):
        row = 5
        for i in range(3):
            self.board[row][i+1] = 2
            row -= 1
        self.board[5][4] = 1
        self.board[4][4] = 2
        self.board[3][4] = 1
        self.board[5][2] = 2
        self.board[5][3] = 2
        self.board[4][3] = 1
        self.board[5][0] = 1
        column, minimax_value = minimax_a_b.minimax(
            self.board, 6, -10000000000, +100000000000, True)
        self.assertEqual(4, column)

    def test_minimax_wins_in_diagonal2(self):
        for i in range(3):
            self.board[i+3][i+2] = 2
        self.board[5][2] = 2
        self.board[5][3] = 1
        self.board[5][1] = 1
        self.board[4][2] = 1
        self.board[5][3] = 1
        self.board[4][1] = 2
        self.board[3][1] = 1

        column, minimax_value = minimax_a_b.minimax(
            self.board, 6, -10000000000, +100000000000, True)
        self.assertEqual(1, column)

    def test_minimax_blocks_opposite_win_in_row(self):
        for i in range(3):
            self.board[5][i+3] = 1
        self.board[5][0] = 2
        self.board[5][2] = 2
        column, minimax_value = minimax_a_b.minimax(
            self.board, 6, -10000000000, +100000000000, True)
        self.assertEqual(6, column)

    def test_minimax_blocks_opposite_win_in_column(self):
        for i in range(3):
            self.board[i+3][2] = 1
        self.board[5][0] = 2
        self.board[5][1] = 2
        column, minimax_value = minimax_a_b.minimax(
            self.board, 6, -10000000000, +100000000000, True)
        self.assertEqual(2, column)

    def test_minimax_blocks_opposite_win_in_diagonal1(self):
        row = 5
        for i in range(3):
            self.board[row][i+1] = 1
            row -= 1
        self.board[5][4] = 2
        self.board[4][4] = 1
        self.board[3][4] = 2
        self.board[5][2] = 1
        self.board[5][3] = 1
        self.board[4][3] = 2
        self.board[5][0] = 2
        column, minimax_value = minimax_a_b.minimax(
            self.board, 6, -10000000000, +100000000000, True)
        self.assertEqual(4, column)

    def test_minimax_blocks_opposite_win_in_diagonal2(self):
        for i in range(3):
            self.board[i+3][i+2] = 1
        self.board[5][2] = 1
        self.board[5][3] = 2
        self.board[5][1] = 2
        self.board[4][2] = 2
        self.board[5][3] = 2
        self.board[4][1] = 1
        self.board[3][1] = 2

        column, minimax_value = minimax_a_b.minimax(
            self.board, 6, -10000000000, +100000000000, True)
        self.assertEqual(1, column)

    def test_minimax_when_board_full(self):
        """
        Koska AI aloittaa, AI:n siirto ei ole ikinä viimeinen täydessä laudassa.
        Eli minimaxia ei ikinä kutsuta, kun lauta on täynnä.
        Tämä testaa että minimax toimii, kun copyboardit täyttyvät.

        """
        board = np.array([
            [1, 2, 1, 2, 1, 0, 0],
            [1, 2, 1, 2, 1, 2, 1],
            [2, 1, 2, 1, 2, 1, 2],
            [2, 1, 2, 1, 2, 1, 2],
            [1, 2, 1, 2, 1, 2, 1],
            [1, 2, 1, 2, 1, 2, 1]])
        column, minimax_value = minimax_a_b.minimax(
            board, 6, -10000000000, +100000000000, True)
        self.assertEqual(5, column)

    def test_win_after_two_steps(self):
        """Tekeekö fiksun siirron joka johtaisi voittoon 2 siirrossa"""
        board = np.array([[0,0,0,0,0,0,0], 
                      [0,0,0,1,0,0,0],
                      [0,0,0,1,0,0,0],
                      [0,0,0,2,1,0,0],
                      [0,2,0,2,1,2,0],
                      [1,1,2,2,2,1,1]])
        column, minimax_value = minimax_a_b.minimax(board, 6, -10000000000, +100000000000, True)
        self.assertEqual(2, column)
    
    def test_blocking_skill_if_player_win_in_two(self):
        """"Tekeekö fiksun siirron joka blokkaisi pelaajan voiton 2 siirrossa"""
        board = np.array([[0,0,0,0,0,0,0], 
                      [0,0,0,0,0,0,0],
                      [0,0,0,0,0,0,0],
                      [0,0,1,0,1,0,1],
                      [0,2,2,1,1,2,1],
                      [1,1,2,2,2,1,2]])
        column, minimax_value = minimax_a_b.minimax(board, 6, -10000000000, +100000000000, True)
        self.assertEqual(3, column)

class TestMinimaxHelpFunctions(unittest.TestCase):
    """
    Testataan minimax-algoritmiin liittyviä metodeja ja apufunktioita. 
    """

    def setUp(self):
        self.turn = 1
        self.board = functions.create_the_board()

    def test_get_possible_columns(self):
        self.assertEqual(functions.get_possible_columns(
            self.board), [3, 2, 4, 1, 5, 0, 6])
        for i in range(7):
            self.board[0][i] = 1
        self.assertEqual(functions.get_possible_columns(self.board), [])

    def test_returns_next_empty_row_correctly(self):
        self.assertEqual(functions.next_empty_row(self.board, 3), 5)
        for i in range(7):
            self.board[5][i] = 1
        self.assertEqual(functions.next_empty_row(self.board, 3), 4)

    def test_checks_terminal_node_correctly(self):
        self.assertFalse(minimax_a_b.check_if_terminal_node(self.board, 3))

        for i in range(0, 4):
            self.board[i][6] = 2
        self.assertEqual(minimax_a_b.check_if_terminal_node(
            self.board, 3), (None, 2000))

        self.board[0][6] = 0  # poistetaan voittorivi
        for i in range(0, 4):
            self.board[3][i] = 1
        self.assertEqual(minimax_a_b.check_if_terminal_node(
            self.board, 3), (None, -2000))

    def test_checks_terminal_node_correctly_low_depth(self):
        for i in range(0, 4):
            self.board[i][6] = 2
        self.assertEqual(minimax_a_b.check_if_terminal_node(
            self.board, 5), (None, 3000))

        self.board[0][6] = 0  # poistetaan voittorivi
        for i in range(0, 4):
            self.board[3][i] = 1
        self.assertEqual(minimax_a_b.check_if_terminal_node(
            self.board, 4), (None, -3000))

    def test_heuristic_row_win(self):
        self.assertEqual(minimax_a_b.heuristic_value(self.board, 2), 0)
        for i in range(4):
            self.board[5][i] = 2
        self.assertEqual(minimax_a_b.heuristic_value(self.board, 2), 300)

    def test_heuristic_opposite_player_row_win(self):
        self.assertEqual(minimax_a_b.heuristic_value(self.board, 2), 0)
        for i in range(4):
            self.board[5][i] = 1
        self.assertEqual(minimax_a_b.heuristic_value(self.board, 2), -150)

    def test_heuristic_column_win(self):
        for i in range(4):
            self.board[i][4] = 2
        self.assertEqual(minimax_a_b.heuristic_value(self.board, 2), 300)

    def test_heuristic_opposite_player_column_win(self):
        self.assertEqual(minimax_a_b.heuristic_value(self.board, 2), 0)
        for i in range(4):
            self.board[i][2] = 1
        self.assertEqual(minimax_a_b.heuristic_value(self.board, 2), -150)

    def test_heuristic_diagonal1_win(self):
        row = 5
        for i in range(4):
            self.board[row][i] = 2
            row -= 1
        self.assertEqual(minimax_a_b.heuristic_value(self.board, 2), 300)

    def test_heuristic_opposite_player_diagonal1_win(self):
        row = 5
        for i in range(4):
            self.board[row][i] = 1
            row -= 1
        self.assertEqual(minimax_a_b.heuristic_value(self.board, 2), -150)

    def test_heuristic_diagonal2_win(self):
        for i in range(4):
            self.board[i][i] = 2
        self.assertEqual(minimax_a_b.heuristic_value(self.board, 2), 300)

    def test_heuristic_opposite_player_diagonal2_win(self):
        for i in range(4):
            self.board[i][i] = 1
        self.assertEqual(minimax_a_b.heuristic_value(self.board, 2), -150)
