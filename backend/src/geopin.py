from flask import Flask
from services.database_service import connect_to_database

app = Flask(__name__)

connect_to_database()

import resources.rounds
import resources.maps