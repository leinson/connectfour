import unittest
import functions
import numpy as np


class TestFunctions(unittest.TestCase):
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

    def test_check_if_no_win_player(self):
        self.assertFalse(functions.check_if_win(self.board, 0, (3, 0)))


#    def test_ai_choose_column_correctly(self):
#        pass
#    def test_check_if_row_win(self):
#        pass
#    def test_check_if_column_win(self):
#        pass
