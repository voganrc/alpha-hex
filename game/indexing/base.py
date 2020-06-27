from abc import ABC, abstractmethod


class Grid(ABC):
    N_ROWS = None
    N_COLS = None
    INDICES = None

    @abstractmethod
    def __init__(self):
        raise NotImplementedError

    def get(self, row, col):
        if not self.__class__.in_bounds(row, col):
            return None
        idx = self.__class__.INDICES[row][col]
        if idx is None:
            return None
        return self.elements[idx]

    @classmethod
    def in_bounds(cls, row, col):
        return 0 <= row < cls.N_ROWS and 0 <= col < cls.N_COLS
