from src.Board import Board
from src.Game import Game
from src.Tetromino import Tetromino
import random


class TetrisGame(Game):
    def __init__(self, width=20, height=20):
        self.width = width
        self.height = height
        self.board = Board(width, height)
        self.Tetromino = self.generate_tetromino()
        self.current_tetromino = random.choice(list(Tetromino))
        self.current_position = (width // 2, 0)
        self.score = 0

    def generate_tetromino(self):
        return random.choice(list(Tetromino))

    def actions(self, state):
        """Return a collection of allowable moves for the current Tetromino."""
        moves = []
        for dx in [-1, 0, 1]:  # Left, stay, right
            new_position = (self.current_position[0] + dx, self.current_position[1] + 1)
            if not state.check_collision(self.current_tetromino, new_position):
                moves.append(new_position)
        return moves

    def result(self, state, move):
        """Return the state that results from making a move."""
        new_board = state.new({})
        new_board.place_tetromino(self.current_tetromino, move)
        cleared_rows = new_board.clear_rows()
        self.score += 50 * cleared_rows
        if cleared_rows > 1:
            self.score += int((cleared_rows * 0.1) * self.width * cleared_rows)
        self.current_tetromino = random.choice(list(Tetromino))
        self.current_position = (state.width // 2, 0)
        return new_board

    def is_terminal(self, state):
        """Return True if the game is over."""
        return state.check_collision(self.current_tetromino, self.current_position)

    def utility(self, state, player=None):
        """Return the score as the utility of the state."""
        return self.score

    def move_tetromino(self, direction):
        """Move the current tetromino in the given direction."""
        new_position = (self.current_position[0] + direction[0], self.current_position[1] + direction[1])
        if not self.board.check_collision(self.current_tetromino, new_position):
            self.current_position = new_position
            return True
        return False

    def place_tetromino(self):
        """Place the current tetromino on the board."""
        for x, y in self.current_tetromino.value:
            board_x = self.current_position[0] + x
            board_y = self.current_position[1] + y
            self.board.set_cell(board_x, board_y, 1)

    def clear_rows(self):
        """Clear full rows and shift rows above down."""
        new_grid = [[0 for _ in range(self.width)] for _ in range(self.height)]
        new_row_index = self.height - 1

        for row_index in range(self.height - 1, -1, -1):
            if all(self.board.grid[row_index]):
                continue
            new_grid[new_row_index] = self.board.grid[row_index]
            new_row_index -= 1

        self.board.grid = new_grid

    def is_game_over(self):
        for cell in self.board.grid[0]:
            if cell != 0:
                self.game_over = True
                return True
        return False