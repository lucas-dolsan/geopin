from database import database
import random

from models.place import Place
from models.coords import Coords

places = [
    Place(
        id='f26d60305dae929ef8640a75e70dd78ab809cfe9',
        coords=Coords(lat=37.869085, lng=-122.254775)
    ),
    Place(
        id='f26d60305dae929ef8640a75e70dd78ab809cfe9',
        coords=Coords(lat=37.869085, lng=-122.254775)
    ),
]

class PlacesMock():
    @staticmethod
    def get_all_places():
        collection = database.client[database.DATABASE_NAME]['collection']
        collection.insert_one({"id": 1})
        res=collection.find_one()
        return res

    @staticmethod
    def get_random_place():
        return places[random.randint(0, len(places) - 1)]

