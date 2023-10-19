class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'

    def print_board(self):
        """Print the current game board."""
        for row in self.board:
            print(" | ".join(row))
            print("-" * 9)

    def make_move(self, row, col):
        """Make a move on the board."""
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
        else:
            raise ValueError("Invalid move. Try again.")

    def check_winner(self):
        """Check if the current player has won."""
        for row in self.board:
            if all(cell == self.current_player for cell in row):
                return True

        for col in range(3):
            if all(self.board[row][col] == self.current_player for row in range(3)):
                return True

        if all(self.board[i][i] == self.current_player for i in range(3)) or all(
                self.board[i][2 - i] == self.current_player for i in range(3)):
            return True

        return False

    def is_board_full(self):
        """Check if the board is full (a draw)."""
        return all(cell != ' ' for row in self.board for cell in row)

    def play_game(self):
        """Play the Tic-Tac-Toe game."""
        while True:
            self.print_board()
            try:
                row, col = map(int, input(f"Player {self.current_player}, enter your move (row and column): ").split())
                self.make_move(row, col)
            except (ValueError, IndexError):
                print("Invalid input. Try again.")
                continue

            if self.check_winner():
                self.print_board()
                print(f"Player {self.current_player} wins!")
                break

            if self.is_board_full():
                self.print_board()
                print("It's a draw!")
                break

            self.current_player = 'O' if self.current_player == 'X' else 'X'


if __name__ == "__main__":
    game = TicTacToe()
    game.play_game()
