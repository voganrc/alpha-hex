from abc import ABC

from game.pieces.resource import Resource


class Tile(ABC):

    def __init__(self, hex_) -> None:
        self.hex_ = hex_
        self.number = None


class HillsTile(Tile):
    COUNT = 3
    RGB = (193, 67, 55)
    RESOURCE = Resource.BRICK


class ForestTile(Tile):
    COUNT = 4
    RGB = (39, 110, 52)
    RESOURCE = Resource.LUMBER


class MountainsTile(Tile):
    COUNT = 3
    RGB = (181, 182, 184)
    RESOURCE = Resource.ORE


class FieldsTile(Tile):
    COUNT = 4
    RGB = (254, 215, 59)
    RESOURCE = Resource.GRAIN


class PastureTile(Tile):
    COUNT = 4
    RGB = (159, 199, 70)
    RESOURCE = Resource.WOOL


class DesertTile(Tile):
    COUNT = 1
    RGB = (248, 199, 96)
    RESOURCE = None
