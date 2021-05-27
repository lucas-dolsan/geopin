from mongoengine.connection import ConnectionFailure
import pymongo
from enum import Enum
from settings.database_settings import settings
import mongoengine 

def print_database_settings(settings):
    print('Connecting to database using the following settings:')
    for key in settings.keys():
        print(f'{key}={settings[key]}')
    print('\n')

def test_database_connection(connection: pymongo.MongoClient):
        try:
            connection.server_info() 
            print('Sucessfully connected to the database \n')
        except pymongo.errors.ServerSelectionTimeoutError:
            print('Failed to connect to the database \n')


def connect_to_database():
        print_database_settings(settings)
        connection = mongoengine.connect(
            settings['DATABASE_NAME'],
            host=settings['DATABASE_HOST'],
            port=settings['DATABASE_PORT'],
            serverSelectionTimeoutMS=1500
        )
        test_database_connection(connection)

