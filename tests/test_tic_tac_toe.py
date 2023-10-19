import unittest
from io import StringIO
import sys
from tic_tac_toe.tic_tac_toe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    def setUp(self):
        self.game = TicTacToe()

    def test_print_board(self):
        captured_output = StringIO()
        sys.stdout = captured_output
        self.game.print_board()
        sys.stdout = sys.__stdout__
        expected_output = " | | \n---------\n | | \n---------\n | | \n---------\n"
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_make_move(self):
        self.game.make_move(0, 0)
        self.assertEqual(self.game.board[0][0], 'X')

        with self.assertRaises(ValueError):
            self.game.make_move(0, 0)

    def test_check_winner(self):
        self.game.board = [['X', 'X', 'X'], [' ', ' ', 'O'], ['O', ' ', ' ']]
        self.assertTrue(self.game.check_winner())

        self.game.board = [['X', 'O', 'O'], [' ', 'X', 'O'], ['O', ' ', 'X']]
        self.assertTrue(self.game.check_winner())

        self.game.board = [['O', 'O', 'X'], ['O', 'X', ' '], ['X', ' ', 'O']]
        self.assertTrue(self.game.check_winner())

    def test_is_board_full(self):
        self.game.board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'X']]
        self.assertTrue(self.game.is_board_full())

        self.game.board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', ' ']]
        self.assertFalse(self.game.is_board_full())

if __name__ == "__main__":
    unittest.main()
