from http import HTTPStatus
from lib.response import Response
from models.place import Place

class RoundsController():

    @staticmethod
    def get_rounds():
        place = Place.objects[0]
        return Response(place, status=HTTPStatus.OK)
