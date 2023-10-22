import unittest
from io import StringIO
import sys
from tic_tac_toe.tic_tac_toe import TicTacToe

class TestTicTacToe(unittest.TestCase):
    """
    A unit test class for the TicTacToe game.
    This class contains test cases to verify the functionality of the TicTacToe class.

    """
    def setUp(self):
        """
        Set up test environment for each test case.

        This method is called before each individual test case to prepare the testing environment.
        It creates an instance of the TicTacToe class, which can be used for testing.

        """
        self.game = TicTacToe()  # Create an instance of the TicTacToe class for testing

    def test_print_board(self):
        """
        Test the 'print_board' method of the TicTacToe class.
    
        This test case captures the printed output of the 'print_board' method and compares it with the
        expected output to verify that the method correctly displays the Tic-Tac-Toe game board.
    
    """
        # Capture the standard output (print) to a StringIO buffer for testing.
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the 'print_board' method to print the Tic-Tac-Toe game board.
        self.game.print_board()

        # Restore the original standard output.
        sys.stdout = sys.__stdout__

        # Define the expected output for an empty game board.
        expected_output = "  |   |  \n---------\n  |   |  \n---------\n  |   |  \n---------\n"
        
         # Check if the captured output matches the expected output.
        self.assertEqual(captured_output.getvalue(), expected_output)

    def test_make_move(self):
        """
        Test the 'make_move' method of the TicTacToe class.
    
        This test case checks the behavior of the 'make_move' method by making valid and invalid moves and
        verifying that the board is updated correctly and that it raises an exception for an invalid move.

    """
        # Make a valid move for 'X' at row 0, column 0.
        self.game.make_move(0, 0)

        # Check if the board was updated correctly, and the specified cell contains 'X'.
        self.assertEqual(self.game.board[0][0], 'X')

        # Attempt to make another move at the same position, which should be invalid.
        # Verify that the 'make_move' method raises a ValueError.
        with self.assertRaises(ValueError):
            self.game.make_move(0, 0)


    def test_check_winner(self):
        """
        Test the 'check_winner' method of the TicTacToe class.
    
        This test case checks the 'check_winner' method for various winning scenarios.
        It sets up different board configurations where 'X' or 'O' wins and verifies that the method returns True.

    """
        # Test case 1: 'X' wins horizontally in the top row.
        self.game.board = [['X', 'X', 'X'], [' ', ' ', 'O'], ['O', ' ', ' ']]
        self.assertTrue(self.game.check_winner())

        # Test case 2: 'X' wins diagonally from top-left to bottom-right.
        self.game.board = [['X', 'O', 'O'], [' ', 'X', 'O'], ['O', ' ', 'X']]
        self.assertTrue(self.game.check_winner())

        # Test case 3: 'O' wins vertically in the left column.
        self.game.board = [['O', 'O', 'X'], ['O', 'X', ' '], ['X', ' ', 'O']]
        self.assertTrue(self.game.check_winner())



    def test_is_board_full(self):
        """
        Test the 'is_board_full' method of the TicTacToe class.
    
        This test case checks the 'is_board_full' method for two different board configurations:
        one where the board is full (a draw) and another where there are still empty spaces.
        It verifies that the method returns True for a full board and False otherwise.
    """
        # Test case 1: A full board (a draw) with no empty spaces.
        self.game.board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', 'X']]
        self.assertTrue(self.game.is_board_full())
     
        # Test case 2: A partially filled board with some empty spaces.
        self.game.board = [['X', 'O', 'X'], ['O', 'X', 'O'], ['O', 'X', ' ']]
        self.assertFalse(self.game.is_board_full())



    def test_play_game(self):
        """
        Test the 'play_game' method of the TicTacToe class.
        This test case simulates a game where 'X' wins and verifies that the game outcome matches the expected output.
    
    """
        # Simulate a game where 'X' wins
        user_inputs = ['0 0', '0 1', '1 0', '1 1', '2 0']

        # Define the expected output to match the game simulation
        expected_output = (
            "  |   |  \n---------\n  |   |  \n---------\n  |   |  \n---------\n"
            "Player X, enter your move (row and column): "
            "X |   |  \n---------\n  |   |  \n---------\n  |   |  \n---------\n"
            "Player O, enter your move (row and column): "
            "X | O |  \n---------\n  |   |  \n---------\n  |   |  \n---------\n"
            "Player X, enter your move (row and column): "
            "X | O |  \n---------\nX |   |  \n---------\n  |   |  \n---------\n"
            "Player O, enter your move (row and column): "
            "X | O |  \n---------\nX | O |  \n---------\n  |   |  \n---------\n"
            "Player X, enter your move (row and column): "
            "X | O |  \n---------\nX | O |  \n---------\nX |   |  \n---------\n"
            "Player X wins!\n"
        )

        # Capture the standard output and input to simulate the game
        captured_output = StringIO()
        captured_input = StringIO("\n".join(user_inputs)) # Join the user inputs with newlines
        sys.stdout = captured_output
        sys.stdin = captured_input

        # Call the 'play_game' method to simulate the game
        self.game.play_game()
        self.maxDiff = None

        # Restore the original standard output and input
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

        # Verify that the captured output matches the expected output
        self.assertEqual(captured_output.getvalue(), expected_output)


if __name__ == "__main__":
    # This block of code is executed only if this Python script is run as the main program.
    # Run the unit tests defined in this script using the unittest module.
    unittest.main()
