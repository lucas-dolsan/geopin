from flask import Flask
from services.database_service import DatabaseService

app = Flask(__name__)

DatabaseService.connect_to_database()

import resources.rounds
import resources.maps

if __name__ == "__main__":
    app.run(debug=True)
from models.map import Map
Map.objects.filter()
