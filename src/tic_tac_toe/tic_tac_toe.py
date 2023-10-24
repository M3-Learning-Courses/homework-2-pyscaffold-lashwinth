class TicTacToe:
    def __init__(self):
        "Initialize the Tic-Tac-Toe game board as a 3x3 grid with empty spaces."
        self.board = [[' ' for _ in range(3)] for _ in range(3)]

        # Set the starting player to 'X'. 
        # 'X' usually starts in the standard game of Tic-Tac-Toe.
        self.current_player = 'X'

    def print_board(self):
        """
        Print the current game board.

        This method is responsible for displaying the current state of the Tic-Tac-Toe board.
        It prints the board's grid structure with 'X', 'O', and empty spaces (' ') to represent
        the moves made by the players.

        Example output:
        | X | O | X
        ---------
        | O | X | O
        ---------
        | O | X |  

        """
        for row in self.board:
            print(" | ".join(row)) # Print a row of cells with vertical bars between them
            print("-" * 9)         # Print a horizontal line to separate rows

    def make_move(self, row, col):
        """
        Make a move on the board.
        This method allows a player to make a move on the Tic-Tac-Toe board by specifying
        the row and column where they want to place their symbol ('X' or 'O'). If the
        specified cell is empty (' '), the move is valid and the player's symbol is placed
        in that cell. If the cell is already occupied, it raises a ValueError indicating an
        invalid move.

        Parameters:
        - row (int): The row where the player wants to place their symbol (0-based index).
        - col (int): The column where the player wants to place their symbol (0-based index).
    
        Raises:
        - ValueError: If the specified cell is already occupied by a player's symbol.
    
        Example usage:
        make_move(1, 2)  # Places the current player's symbol in the cell at row 1, column 2.
        make_move(0, 0)  # Raises a ValueError if the cell at row 0, column 0 is already occupied.

        """
        if self.board[row][col] == ' ':
            # If the specified cell is empty, place the current player's symbol.
            self.board[row][col] = self.current_player
        else:
            # If the cell is already occupied, raise a ValueError indicating an invalid move.
            raise ValueError("Invalid move. Try again.")

    def check_winner(self):
        """
        Check if the current player has won the game.
    
        This method checks the Tic-Tac-Toe board to determine if the current player ('X' or 'O') has
        achieved a winning combination, either horizontally, vertically, or diagonally. If a winning
        combination is found, the method returns True; otherwise, it returns False.
    
        Returns:
        - bool: True if the current player has won, False otherwise.
    
        Example usage:
        if check_winner():
            print(f"Player {self.current_player} wins!")

        """
        # Check for a horizontal win: all cells in a row contain the current player's symbol.
        for row in self.board:
            if all(cell == self.current_player for cell in row):
                return True

        # Check for a vertical win: all cells in a column contain the current player's symbol.
        for col in range(3):
            if all(self.board[row][col] == self.current_player for row in range(3)):
                return True
        
        # Check for diagonal wins: both diagonals have the current player's symbol.
        if all(self.board[i][i] == self.current_player for i in range(3)) or all(
                self.board[i][2 - i] == self.current_player for i in range(3)):
            return True

         # If no winning combination is found, return False.
        return False


    def is_board_full(self):
        """
        Check if the Tic-Tac-Toe board is full, indicating a draw.
    
        This method examines the Tic-Tac-Toe board to determine if it is completely filled with player symbols
        ('X' and 'O') or if there are no more empty spaces (' '). If the board is full, it means the game
        has ended in a draw.
    
        Returns:
        - bool: True if the board is full (a draw), False otherwise.
    
        Example usage:
        if is_board_full():
            print("It's a draw!")
    
        """
        # Use a list comprehension to check if there are no empty spaces (' ') in the entire board.
        # If all cells are filled, it means the board is full, and the game is a draw.
        return all(cell != ' ' for row in self.board for cell in row)

    def play_game(self):
        """
        Play the Tic-Tac-Toe game.
    
        This method is the core of the Tic-Tac-Toe game. It allows two players to take turns making moves,
        checks for a winner, and handles game termination conditions such as a win or a draw.
    
        The game continues until a player wins or the board is full, resulting in a draw.
    
        Example usage:
        game = TicTacToe()
        game.play_game()
    
        """
        while True:
            self.print_board() # Display the current state of the game board
            try:
                # Prompt the current player to enter their move as 'row' and 'column'.
                row, col = map(int, input(f"Player {self.current_player}, enter your move (row and column): ").split())
                self.make_move(row, col) # Attempt to make the move
            except (ValueError, IndexError):
                print("Invalid input. Try again.")
                continue

            # Check if the current player has won
            if self.check_winner():
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break

            # Check if the board is full (a draw)
            if self.is_board_full():
                self.print_board()
                print("It's a draw!")
                break

            # Switch to the other player for the next turn
            self.current_player = 'O' if self.current_player == 'X' else 'X'


if __name__ == "__main__":
    # This block of code is executed only if this Python script is run as the main program.

    game = TicTacToe() # Create an instance of the TicTacToe class to start a new game.
    game.play_game()   # Call the play_game method to begin the Tic-Tac-Toe game.
