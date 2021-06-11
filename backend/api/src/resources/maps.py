from http import HTTPStatus
from geopin import app
from controllers.map_controller import MapController
from flask import request

from lib.response import Response

@app.route("/maps", methods=['GET', 'POST'])
def get_maps():
    if request.method == "GET":
        return MapController.get_maps()
    if request.method == "POST":
        return MapController.create_map()
    return Response(status=HTTPStatus.METHOD_NOT_ALLOWED)

@app.route("/maps/<id>", methods=['GET','PATCH', 'DELETE'])
def get_map(id: str):
    if request.method == "GET":
        return MapController.get_map(id)
    if request.method == "PATCH":
        return MapController.update_map(id)
    if request.method == "DELETE":
        return MapController.delete_map(id)
    return Response(status=HTTPStatus.METHOD_NOT_ALLOWED)
