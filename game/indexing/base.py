from abc import ABC, abstractmethod


class Grid(ABC):
    N_ROWS = None
    N_COLS = None

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @classmethod
    def in_bounds(cls, row, col):
        return 0 <= row < cls.N_ROWS and 0 <= col < cls.N_COLS
