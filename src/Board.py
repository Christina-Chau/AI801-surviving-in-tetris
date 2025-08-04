# Python
class Board:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0 for _ in range(width)] for _ in range(height)]

    def check_collision(self, tetromino, position):
        """Check if the tetromino collides with the board boundaries or existing blocks."""
        for x, y in tetromino.value:
            board_x = position[0] + x
            board_y = position[1] + y
            if board_x < 0 or board_x >= self.width or board_y < 0 or board_y >= self.height:
                return True  # Collision with boundaries
            if self.grid[board_y][board_x] != 0:
                return True  # Collision with existing blocks
        return False

    def get_cell(self, x, y):
        """Retrieve the value of a cell at the given coordinates."""
        return self.grid[y][x]

    def set_cell(self, x, y, value):
        """Set the value of a cell at the given coordinates."""
        self.grid[y][x] = value