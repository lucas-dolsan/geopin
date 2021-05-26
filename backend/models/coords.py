from lib.json_serializable import JsonSerializable

class Coords(JsonSerializable):
    def __init__(self, lat: float, lng: float):
        self.lat = lat
        self.lng = lng

    def toJson(self):
        return super().toJson()