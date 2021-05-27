
from http import HTTPStatus
from mongoengine.document import Document
from mongoengine.queryset.queryset import QuerySet
import json

class Response():
    response_headers={'Content-Type': 'application/json'}

    def __new__(self, data=None, status=HTTPStatus.OK) -> tuple:
        if data is None:
            data = json.dumps(None)

        if issubclass(data.__class__, (Document, QuerySet)):
            data=data.to_json()

        return data, status, self.response_headers
