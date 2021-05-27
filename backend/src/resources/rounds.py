from geopin import app

from controllers.rounds_controller import RoundsController

@app.route("/rounds")
def get_rounds():
    return RoundsController.get_rounds()
