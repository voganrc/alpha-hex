from abc import ABC
from abc import abstractmethod
from typing import Optional
from enum import Enum


class Resource(Enum):
    BRICK = 0
    LUMBER = 1
    ORE = 2
    GRAIN = 3
    WOOL = 4


class Tile(ABC):

    @abstractmethod
    def __init__(self, hex_x: int, hex_y: int) -> None:
        self._hex_x = hex_x
        self._hex_y = hex_y

    @property
    def hex_x(self) -> int:
        return self._hex_x

    @property
    def hex_y(self) -> int:
        return self._hex_y


class HillsTile(Tile):

    COUNT = 3
    RGB = (193, 67, 55)
    RESOURCE = Resource.BRICK

    def __init__(self, hex_x: int, hex_y: int) -> None:
        super().__init__(hex_x, hex_y)


class ForestTile(Tile):

    COUNT = 4
    RGB = (39, 110, 52)
    RESOURCE = Resource.LUMBER

    def __init__(self, hex_x: int, hex_y: int) -> None:
        super().__init__(hex_x, hex_y)


class MountainsTile(Tile):

    COUNT = 3
    RGB = (181, 182, 184)
    RESOURCE = Resource.ORE

    def __init__(self, hex_x: int, hex_y: int) -> None:
        super().__init__(hex_x, hex_y)


class FieldsTile(Tile):

    COUNT = 4
    RGB = (254, 215, 59)
    RESOURCE = Resource.GRAIN

    def __init__(self, hex_x: int, hex_y: int) -> None:
        super().__init__(hex_x, hex_y)


class PastureTile(Tile):

    COUNT = 4
    RGB = (159, 199, 70)
    RESOURCE = Resource.WOOL

    def __init__(self, hex_x: int, hex_y: int) -> None:
        super().__init__(hex_x, hex_y)


class DesertTile(Tile):

    COUNT = 1
    RGB = (248, 199, 96)
    RESOURCE = None

    def __init__(self, hex_x: int, hex_y: int) -> None:
        super().__init__(hex_x, hex_y)