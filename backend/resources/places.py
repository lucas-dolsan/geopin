from geopin import app

from controllers.places_controller import PlacesController

@app.route("/places")
def get_places():
    return PlacesController.get_places()
