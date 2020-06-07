from abc import ABC
from abc import abstractmethod
from enum import Enum


class Resource(Enum):
    BRICK = 0
    LUMBER = 1
    ORE = 2
    GRAIN = 3
    WOOL = 4


class Vertex:

    def __init__(self):
        self.building = None

        self.n_tile = None
        self.sw_tile = None
        self.se_tile = None

        self.s_tile = None
        self.nw_tile = None
        self.ne_tile = None


class Tile(ABC):

    @abstractmethod
    def __init__(self, hex_x: int, hex_y: int) -> None:
        self.hex_x = hex_x
        self.hex_y = hex_y

        self.nw_vertex = None
        self.n_vertex = None
        self.ne_vertex = None
        self.sw_vertex = None
        self.s_vertex = None
        self.se_vertex = None


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
