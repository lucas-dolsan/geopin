from http import HTTPStatus
from json.decoder import JSONDecodeError
from flask import request
from lib.response import Response
from lib.request_args import RequestArgs
from models.map import Map
from models.place import Place
from mongoengine.errors import DoesNotExist, FieldDoesNotExist, ValidationError
import json

class MapController():
    @staticmethod
    def get_maps():
        try:
            data=Map.objects.filter(**RequestArgs(request.args, Map))
            return Response(data=data, status=HTTPStatus.OK)
        except DoesNotExist:
            return Response(status=HTTPStatus.NOT_FOUND)

    @staticmethod
    def get_map(id: str):
        data=None
        try:
            data=Map.objects.get(id=id)
            return Response(data=data, status=HTTPStatus.OK)

        except (ValidationError, DoesNotExist) as e:
            return Response(status=HTTPStatus.NOT_FOUND)

    @staticmethod
    def delete_map(id: str):
        try:
            map=Map.objects.get(id=id)
            print(map)
            map.delete()
            return Response(status=HTTPStatus.OK)
        except (ValidationError, DoesNotExist) as e:
            return Response(status=HTTPStatus.NOT_FOUND)


    @staticmethod
    def create_map():
        try:
            data=Map(**json.loads(request.data))
            data.validate()
            data.save()
            return Response(data=data, status=HTTPStatus.CREATED)

        except (FieldDoesNotExist, ValidationError, TypeError, JSONDecodeError) as e:
            return Response(status=HTTPStatus.BAD_REQUEST)


    @staticmethod
    def update_map(id: str):
        try:
            data=json.loads(request.data)

            try:
                del data["_id"]
            except KeyError:
                pass

            try:
                map=Map.objects.get(id=id)
                for key in data.keys():
                    map[key] = data[key] 

                map.save()

                return Response(data=map, status=HTTPStatus.OK)
            except (ValidationError, DoesNotExist):
                return Response(status=HTTPStatus.NOT_FOUND)

        except (FieldDoesNotExist, ValidationError, TypeError, JSONDecodeError, KeyError) as e:
            return Response(status=HTTPStatus.BAD_REQUEST)
