from http import HTTPStatus
from lib.response import Response
from models.map import Map
from lib.geo_functions import get_distance_between_locations
from lib.request_args import RequestArgs
from models.place import Place
from services.rounds_service import RoundsService
import random

class RoundsController():

    @staticmethod
    def get_rounds():
        try:
            data=Round.objects.filter(**RequestArgs(request.args, Round))
            return Response(data=data, status=HTTPStatus.OK)
        except DoesNotExist:
            return Response(status=HTTPStatus.NOT_FOUND)

    @staticmethod
    def play_round():
        try:
            data=json.loads(request.data)
            round_id=data['round_id']
            guessed_place=data['guessed_place']
            score=RoundsService.calculate_round_score(round_id, guessed_place)
            next_round=RoundsService.get_players_next_round(current_round_id=round_id)

            round_result={
                'score': score,
                'next_round': next_round
            }
            return Response(round_result, status=HTTPStatus.OK)
        except KeyError:
            return Response(status=HTTPSatus.BAD_REQUEST)

