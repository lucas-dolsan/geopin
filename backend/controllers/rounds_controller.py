from http import HTTPStatus
from lib.json_response import JsonResponse
from services.places_mock import PlacesMock

class RoundsController():

    @staticmethod
    def get_rounds():
        place = PlacesMock.get_random_place()
        return JsonResponse(place, status=HTTPStatus.OK)
