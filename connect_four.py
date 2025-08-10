import numpy as np
class Connect:
    def __init__(self, rows=6, columns=7, turn=1, visited=None):
        self.rows = rows
        self.columns = columns
        self.board = np.zeros((rows, columns), dtype=int)
        self.turn = turn
        self.visited = visited if visited is not None else set()

    def do_move(self, board, col, player):
        """
        Executes the move of each player

        Input
        ------
        board: list of lists
        the matrix representation of the current state

        col: integer
        the desired movement column of the player

        player: integer
        the coresponding player n

        Returns
        -------
        board: list of lists
        The updated state with the movement
        """
        new_board = board.copy()
        if new_board[0, col] != 0:
            return None
        # Check from bottom to up
        for r in range(self.rows - 1, -1, -1):
          # if the space is not occupied
            if new_board[r, col] == 0:
              # put 1 or 2 depending on turn
                new_board[r, col] = player
                return new_board

    def make_move(self, col):
        """
        Calls the move and changes the turn

        Input
        ------
        col: integer
        the desired movement column of the player

        Returns
        -------

        """
      # calls move
        new_b = self.do_move(self.board, col, self.turn)
        # Changes turn
        if new_b is not None:
            self.board = new_b
            self.turn = 3 - self.turn

    def possible_moves(self, board):
        """
        Finds the possible moves for the given state

        Input
        ------
        board: list of lists
        the matrix representation of the current state

        Returns
        -------
        list
        list of possible moves from the given state
        """
      # moves are possible if column is not filled
        return [c for c in range(self.columns) if board[0, c] == 0]

    def terminal(self, board):
        """
        Checks for the terminal state

        Input
        ------
        board: list of lists
        the matrix representation of the current state

        Returns
        -------
        boolean:
        True if there is a win and corresponding winner
        False if the game is not over
        """
        b = board
        R, C = self.rows, self.columns

        # Check for wins (for player 1 and 2)
        for player in [1, 2]:
            # Check horizontal
            for r in range(R):
                for c in range(C - 3):
                    if all(b[r, c + i] == player for i in range(4)):
                        return True, player

            # Check vertical
            for r in range(R - 3):
                for c in range(C):
                    if all(b[r + i, c] == player for i in range(4)):
                        return True, player

            # Check diagonal (down-right)
            for r in range(R - 3):
                for c in range(C - 3):
                    if all(b[r + i, c + i] == player for i in range(4)):
                        return True, player

            # Check diagonal (up-right)
            for r in range(3, R):
                for c in range(C - 3):
                    if all(b[r - i, c + i] == player for i in range(4)):
                        return True, player

        # Check for draw
        if not (b == 0).any():
            return True, 0

        return False, None

    def generate_moves(self, board, depth: int, playermax: bool,
                       alpha=float('-inf'), beta=float('inf')):
        """
        Minimax with alpha beta pruning

        Input
        ------
        board: list of lists
        the matrix representation of the current state

        depth: integer
        the desired max depth level search

        playermax: boolean
        the player's turn: max player or min player

        alpha: float   beta: float
        the parameters for pruning

        Returns
        -------
        value: the corresponding score for minimax
        The updated state with the movement

        best_move: integer
        The best move
        """
        terminal_state, winner = self.terminal(board)
        # Stops when all depth levels explored or leaf is reached
        if depth == 0 or terminal_state:
            return self.score(winner), None

        # Prioritizes moves near center
        # Gets possible moves from the method above
        moves = self.possible_moves(board)
        C = self.columns
        center = C // 2
        moves.sort(key=lambda x: abs(x - center))
        # First player's turn
        if playermax:
          # Initialization
            value, best_move = float('-inf'), None
            for mv in moves:
              # Expands the current state
                child = self.do_move(board, mv, 2)
                if child is None:
                    continue
                # Recursively calls to go deeper
                tmp, _ = self.generate_moves(child, depth - 1, False, alpha, beta)
                # Pruning condition of alpha > beta
                # Max sets max alpha value
                if tmp > value:
                    value, best_move = tmp, mv
                alpha = max(alpha, value)
                if alpha >= beta:
                    break
            return value, best_move
        else:
          # The same logic
            value, best_move = float('inf'), None
            for mv in moves:
                child = self.do_move(board, mv, 1)  # Human is player 1
                if child is None:
                    continue
                tmp, _ = self.generate_moves(child, depth - 1, True, alpha, beta)
                if tmp < value:
                    value, best_move = tmp, mv
                # min player assignmns minimum
                beta = min(beta, value)
                if beta <= alpha:
                    break
            return value, best_move

    def score(self, winner):
        """
        Return corresponding score

        Input
        ------
        winner: integer
        2 for AI 1 for Player

        Returns
        -------
        integer
        1 if AI wins
        -1 for Human
        0 for Draw
        """
        # Scoring for the terminal states
        if winner == 2:
            return 1  # AI wins
        if winner == 1:
            return -1  # Human wins
        return 0  # Draw or non-terminal position

    def iterative_deepening(self, board, max_time=5.0):
        """
        Iteratively explores the states to find the most optimal move

        Input
        ------
        board: list of lists
        the matrix representation of the current state

        time: float
        the desired max time

        Returns
        -------
        best_move : integer
        the corresponding the best move column
        """
        # Used to constraint the search
        start_time = time.time()
        best_move = None
        # Starts from depth = 1
        depth = 1

        while time.time() - start_time < max_time:
            try:
              # For every depth explores the states and calls the minimax algo
                _, move = self.generate_moves(board, depth, playermax=(self.turn == 2))
                best_move = move  # Update our best move
                depth += 1
                # If we're searching very deep, break
                if depth > 15:
                    break
            except:
                break

        print(f"Final search depth: {depth - 1}")
        # If no move was foudn picks the first of possible moves
        if best_move is None and self.possible_moves(board):
            best_move = self.possible_moves(board)[0]

        return best_move
import time
time_keeper = []
# Used to keep track of the time for the Performance test
_original_id = Connect.iterative_deepening
def _timed_iterative_deepening(self, board, max_time=5.0):
    """
    Measures the time required for AI to move

    Input
    ------
    board: list of lists
    the matrix representation of the current state

    time: float
    the desired max time

    Returns
    -------
    best_move : integer
    the corresponding the best move column
    """
    start = time.time()
    move = _original_id(self, board, max_time)
    elapsed = time.time() - start
    time_keeper.append(round(elapsed, 5))
    print(f"[AI] Move took {elapsed:.3f} s")
    return move

Connect.iterative_deepening = _timed_iterative_deepening

def print_board(b):
    """
    Outputs the board

    Input
    ------
    b: list of lists
    the matrix representation of the current state

    Returns
    -------
    Better state illustration
    """
    print()
    # Replaces 1 and 2 by X and O for better user experience
    for r in range(b.shape[0]):
        print(' | '.join(['.' if x == 0 else ('X' if x == 1 else 'O') for x in b[r]]))
    print('-' * (4 * b.shape[1] - 1))
    print(' | '.join([str(i) for i in range(b.shape[1])]))
    print()


if __name__ == "__main__":
  # Welcoming message
    game = Connect()
    print("Welcome to Connect Four!")
    print("You are X, the AI is O")

    # Ask for AI search time
    search_time = 3.0

    # Sets the turn
    ai_first = None
    while ai_first not in ['y', 'n']:
        ai_first = input("Do you want the AI to go first? (y/n): ").lower()

    # Set initial turn based on who goes first
    if ai_first == 'y':
        game.turn = 2  # Player 2 (AI) starts

    while True:
        # Shows the updated board after each move
        print_board(game.board)

        # For the human turn
        if game.turn == 1:
            col = None
            while col not in game.possible_moves(game.board):
                try:
                    col = int(input(f"Your turn (X). Choose column [0–{game.columns - 1}]: "))
                except ValueError:
                    continue
            game.make_move(col)
        else: # For AI turn shows the message
            print("AI is thinking...")
            ai_col = game.iterative_deepening(game.board, max_time=search_time)
            print(f"AI plays column {ai_col}")
            game.make_move(ai_col)

        # Checks for the winner and outputs the corresponding message
        done, winner = game.terminal(game.board)
        if done:
            print_board(game.board)
            if winner == 1:
                print("You win! 🎉")
            elif winner == 2:
                print("AI wins…")
            else:
                print("Draw!")
            break
