class Game:
    def __init__(self):
        # Initialize game state
        self.turn = 'X'
        self.tie = False
        self.winner = None
        self.board = {
            'a1': None, 'b1': None, 'c1': None,
            'a2': None, 'b2': None, 'c2': None,
            'a3': None, 'b3': None, 'c3': None,
        }

    def print_board(self):
        b = self.board
        print(f"""
          A   B   C
      1)  {b['a1'] or ' '} | {b['b1'] or ' '} | {b['c1'] or ' '}
          ----------
      2)  {b['a2'] or ' '} | {b['b2'] or ' '} | {b['c2'] or ' '}
          ----------
      3)  {b['a3'] or ' '} | {b['b3'] or ' '} | {b['c3'] or ' '}
        """)

    def print_message(self):
        if self.tie:
            print("Tie game!")
        elif self.winner:
            print(f"{self.winner} wins the game!")
        else:
            print(f"It's player {self.turn}'s turn!")

    def render(self):
        self.print_board()
        self.print_message()

    def get_move(self):
        while True:
            move = input("Enter a valid move (example: A1): ").lower()
            if move in self.board and self.board[move] is None:
                self.board[move] = self.turn
                break
            else:
                print("Invalid move! Please try again.")

    def check_for_winner(self):
        # List all possible winning combinations
        winning_combinations = [
            ['a1', 'b1', 'c1'],  # top row
            ['a2', 'b2', 'c2'],  # middle row
            ['a3', 'b3', 'c3'],  # bottom row
            ['a1', 'a2', 'a3'],  # left column
            ['b1', 'b2', 'b3'],  # middle column
            ['c1', 'c2', 'c3'],  # right column
            ['a1', 'b2', 'c3'],  # diagonal 1
            ['a3', 'b2', 'c1'],  # diagonal 2
        ]

        for combo in winning_combinations:
            if self.board[combo[0]] and (self.board[combo[0]] == self.board[combo[1]] == self.board[combo[2]]):
                self.winner = self.turn
                return True
        return False

    def check_for_tie(self):
        if all(value is not None for value in self.board.values()) and not self.winner:
            self.tie = True
            return True
        return False

    def switch_turn(self):
        self.turn = 'O' if self.turn == 'X' else 'X'

    def play_game(self):
        print("Welcome to Tic-Tac-Toe!")
        while not (self.winner or self.tie):
            self.render()
            self.get_move()
            if self.check_for_winner():
                break
            if self.check_for_tie():
                break
            self.switch_turn()
        self.render()
        print("Game over!")


# Instantiate and run the game
if __name__ == "__main__":
    game_instance = Game()
    game_instance.play_game()
