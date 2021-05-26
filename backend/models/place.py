from lib.json_serializable import JsonSerializable
from models.coords import Coords

class Place(JsonSerializable):
    def __init__(self, id: str, coords: Coords):
        self.id = id
        self.coords = coords

    def toJson(self):
        return super().toJson()