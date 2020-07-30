from abc import ABC

from game.pieces.resource import Resource


class Tile(ABC):

    def __init__(self, hex_) -> None:
        self.hex_ = hex_
        self.number = None


class HillsTile(Tile):
    COUNT = 3
    RESOURCE = Resource.BRICK


class ForestTile(Tile):
    COUNT = 4
    RESOURCE = Resource.LUMBER


class MountainsTile(Tile):
    COUNT = 3
    RESOURCE = Resource.ORE


class FieldsTile(Tile):
    COUNT = 4
    RESOURCE = Resource.GRAIN


class PastureTile(Tile):
    COUNT = 4
    RESOURCE = Resource.WOOL


class DesertTile(Tile):
    COUNT = 1
    RESOURCE = None
