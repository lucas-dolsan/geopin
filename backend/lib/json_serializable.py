import json

class JsonSerializable(object):
    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)