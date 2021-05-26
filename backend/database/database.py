import pymongo

DATABASE_ADDRESS="172.17.0.4"
DATABASE_PORT="27017"
DATABASE_NAME="geopin_db"

client=pymongo.MongoClient(f"mongodb://{DATABASE_ADDRESS}:{DATABASE_PORT}/")
database=client[DATABASE_NAME]