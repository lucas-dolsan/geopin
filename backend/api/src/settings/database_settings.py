import os
from os.path import join, dirname
from dotenv import load_dotenv

ENV_FILE_NAME='.env'

load_dotenv(join(dirname(__file__), ENV_FILE_NAME))

settings={}

settings['DATABASE_HOST']=os.environ.get("DATABASE_HOST")
settings['DATABASE_NAME']=os.environ.get("DATABASE_NAME")
settings['DATABASE_PORT']=int(os.environ.get("DATABASE_PORT"))
