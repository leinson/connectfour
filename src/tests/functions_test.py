import unittest
import functions
import numpy as np

# TODO:
# Minimaxin testaus

class TestFunctions(unittest.TestCase):
    """Testataan functions.py yleisiä metodeja.

    Args:
        unittest (_type_): _description_
    """

    def setUp(self):
        self.turn = 0
        self.board = functions.create_the_board()

    def test_turn_changes_from_player_to_ai(self):
        turn = 0
        self.assertEqual(functions.change_turn(turn), 1)

    def test_turn_changes_from_ai_to_player(self):
        turn = 1
        self.assertEqual(functions.change_turn(turn), 0)

    def test_creates_the_board_correctly(self):
        testboard = np.zeros((6, 7))
        np.testing.assert_array_equal(testboard, functions.create_the_board())

    def test_choose_column_player_correctly(self):
        np.testing.assert_equal((5, 1), functions.choose_column(1, self.board))


class TestCheckIfWin(unittest.TestCase):
    """
    Testataan check_if_win metodia erilaisissa tilanteissa.
    """

    def setUp(self):
        self.turn = 0
        self.board = functions.create_the_board()

    def test_check_if_no_win_player(self):
        self.assertFalse(functions.check_if_win(self.board, 0, (3, 0)))

    def test_check_if_win_chooses_ai_or_player_correctly(self):
        """
        Luodaan voittorivit molemmille, katsotaan että molemmat
        funktiokutsut löytävät omat voittorivinsä omalla vuoronumerolla.
        """
        for i in range(0, 4):
            self.board[i][0] = 1
        for i in range(0, 4):
            self.board[i][4] = 2
        self.assertTrue(functions.check_if_win(self.board, 0, (0, 0)))
        self.assertTrue(functions.check_if_win(self.board, 1, (0, 4)))

    def test_check_if_row_win_ai(self):
        """
        5-rivin voittotarkistus ai. Testataan myös eri paikat, missä
        voittorivi voi olla.
        """
        for i in range(0, 4):
            self.board[5][i] = 2
        self.assertTrue(functions.check_if_win(self.board, 1, (5, 0)))

        self.board = functions.create_the_board()
        for i in range(1, 5):
            self.board[5][i] = 2
        self.assertTrue(functions.check_if_win(self.board, 1, (5, 3)))

        self.board = functions.create_the_board()
        for i in range(2, 6):
            self.board[5][i] = 2
        self.assertTrue(functions.check_if_win(self.board, 1, (5, 6)))

        self.board = functions.create_the_board()
        for i in range(3, 7):
            self.board[5][i] = 2
        self.assertTrue(functions.check_if_win(self.board, 1, (5, 2)))

    def test_check_if_row_win_player(self):
        """
        5-rivin voittotarkistus pelaajalle. Testataan myös eri paikat, missä
        voittorivi voi olla.
        """
        for i in range(0, 4):
            self.board[5][i] = 1
        self.assertTrue(functions.check_if_win(self.board, 0, (5, 0)))

        self.board = functions.create_the_board()
        for i in range(1, 5):
            self.board[5][i] = 1
        self.assertTrue(functions.check_if_win(self.board, 0, (5, 3)))

        self.board = functions.create_the_board()
        for i in range(2, 6):
            self.board[5][i] = 1
        self.assertTrue(functions.check_if_win(self.board, 0, (5, 6)))

        self.board = functions.create_the_board()
        for i in range(3, 7):
            self.board[5][i] = 1
        self.assertTrue(functions.check_if_win(self.board, 0, (5, 2)))

    def test_check_if_column_win(self):
        """Testi 0 sarakkeelle voitosta.
        """
        for i in range(0, 4):
            self.board[i][0] = 1
        self.assertTrue(functions.check_if_win(self.board, 0, (0, 0)))

    def test_check_if_diagonal_1_win(self):
        row = 5
        for i in range(0, 4):
            self.board[row][i] = 1
            row -= 1
        self.assertTrue(functions.check_if_win(self.board, 0, (5, 0)))

    def test_check_if_diagonal_2_win(self):
        for i in range(0, 4):
            self.board[i][i] = 2
        self.assertTrue(functions.check_if_win(self.board, 1, (0, 0)))

    def test_row_win_in_minimax(self):
        for i in range(0, 4):
            self.board[5][i] = 1
        self.assertTrue(functions.check_if_win(self.board, 0, (-1, -1)))

    def test_column_win_in_minimax(self):
        for i in range(0, 4):
            self.board[i][3] = 1
        self.assertTrue(functions.check_if_win(self.board, 0, (-1, -1)))


class TestMinimax(unittest.TestCase):
    """
    Testataan minimax-algoritmiin liittyviä metodeja ja apufunktioita. 
    """

    def setUp(self):
        self.turn = 1
        self.board = functions.create_the_board()

    def test_get_possible_columns(self):
        self.assertEqual(functions.get_possible_columns(self.board), [3, 2, 4, 1, 5, 0, 6])
        for i in range(7):
            self.board[0][i] = 1
        self.assertEqual(functions.get_possible_columns(self.board), [])

    def test_returns_next_empty_row_correctly(self):
        self.assertEqual(functions.next_empty_row(self.board, 3), 5)
        for i in range(7):
            self.board[5][i] = 1
        self.assertEqual(functions.next_empty_row(self.board, 3), 4)

    def test_checks_terminal_node_correctly(self):
        self.assertFalse(functions.check_if_terminal_node(self.board))
        for i in range(0, 4):
            self.board[i][6] = 2
        self.assertTrue(functions.check_if_terminal_node(self.board))
        for i in range(0, 4):
            self.board[3][i] = 1
        self.assertTrue(functions.check_if_terminal_node(self.board))
        for i in range(7):
            self.board[0][i] = 1
        self.assertTrue(functions.check_if_terminal_node(self.board))
    
    def test_heuristic_row_win(self):
        self.assertEqual(functions.heuristic_value(self.board, 2), 0)
        for i in range(4):
            self.board[5][i] = 2
        self.assertEqual(functions.heuristic_value(self.board, 2), 200)
    
    def test_heuristic_opposite_player_row_win(self):
        self.assertEqual(functions.heuristic_value(self.board, 2), 0)
        for i in range(4):
            self.board[5][i] = 1
        self.assertEqual(functions.heuristic_value(self.board, 2), -100)
    
    def test_heuristic_row_tie(self):
        for i in range(4):
            self.board[5][i] = 1
            self.board[3][i] = 2
        self.assertEqual(functions.heuristic_value(self.board, 2), 50)

    def test_heuristic_column_win(self):
        for i in range(4):
            self.board[i][4] = 2
        self.assertEqual(functions.heuristic_value(self.board, 2), 200)
    
    def test_heuristic_opposite_player_column_win(self):
        self.assertEqual(functions.heuristic_value(self.board, 2), 0)
        for i in range(4):
            self.board[i][2] = 1
        self.assertEqual(functions.heuristic_value(self.board, 2), -100)
    
    def test_heuristic_diagonal1_win(self):
        row = 5
        for i in range(4):
            self.board[row][i] = 2
            row -= 1
        self.assertEqual(functions.heuristic_value(self.board, 2), 200)

    def test_heuristic_opposite_player_diagonal1_win(self):
        row = 5
        for i in range(4):
            self.board[row][i] = 1
            row -= 1
        self.assertEqual(functions.heuristic_value(self.board, 2), -100)

    def test_heuristic_diagonal2_win(self):
        for i in range(4):
            self.board[i][i] = 2
        self.assertEqual(functions.heuristic_value(self.board, 2), 200)

    def test_heuristic_opposite_player_diagonal2_win(self):
        for i in range(4):
            self.board[i][i] = 1
        self.assertEqual(functions.heuristic_value(self.board, 2), -100)
