from http import HTTPStatus
from services.places_mock import PlacesMock
from lib.json_response import JsonResponse

class PlacesController():

    @staticmethod
    def get_places():
        places = PlacesMock.get_all_places()
        return JsonResponse(places, status=HTTPStatus.OK)
