from enum import Enum


class Tetromino(Enum):
    LINE_HORIZONTAL = [(0, 0), (1, 0), (2, 0), (3, 0)]
    LINE_VERTICAL = [(0, 0), (0, 1), (0, 2), (0, 3)]
    L_SHAPE_RIGHT = [(0, 0), (1, 0), (2, 0), (2, 1)]
    L_SHAPE_LEFT = [(0, 1), (0, 0), (1, 0), (2, 0)]
    SQUARE = [(0, 0), (1, 0), (0, 1), (1, 1)]
    Z_SHAPE_RIGHT = [(0, 0), (1, 0), (1, 1), (2, 1)]
    Z_SHAPE_LEFT = [(1, 0), (2, 0), (0, 1), (1, 1)]
