from abc import ABC, abstractmethod


class Grid(ABC):
    N_ROWS = None
    N_COLS = None
    INDICES = None

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    @property
    @abstractmethod
    def elements(self):
        raise NotImplementedError

    def get(self, row, col):
        if not Grid.in_bounds(row, col):
            return None
        idx = Grid.INDICES[row][col]
        if idx is None:
            return None
        return self.elements[idx]

    @classmethod
    def in_bounds(cls, row, col):
        return 0 <= row < cls.N_ROWS and 0 <= col < cls.N_COLS
