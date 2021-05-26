
from lib.json_serializable import JsonSerializable
from http import HTTPStatus
from bson import json_util

class JsonResponse():
    def __new__(self, data=None, status=HTTPStatus.OK) -> tuple:
        if data is None:
            data = "{}"
            return data, status, {'Content-Type': 'application/json'}


        if type(data) is dict:
            return json_util.dumps(data), status, {'Content-Type': 'application/json'}

        if type(data) is tuple or type(data) is list:
            data=list(map(lambda x : x.toJson() if issubclass(x.__class__, JsonSerializable) else x, data)).__str__()
            return data, status, {'Content-Type': 'application/json'}


        if issubclass(data.__class__, JsonSerializable):
            data=data.toJson()
            return data, status, {'Content-Type': 'application/json'}