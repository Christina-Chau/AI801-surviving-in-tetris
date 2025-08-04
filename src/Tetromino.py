from enum import Enum


class Tetromino(Enum):
    LINE = [(0, 0), (1, 0), (2, 0), (3, 0)]
    L_SHAPE = [(0, 0), (1, 0), (2, 0), (2, 1)]
    SQUARE = [(0, 0), (1, 0), (0, 1), (1, 1)]
    Z_SHAPE = [(0, 0), (1, 0), (1, 1), (2, 1)]
