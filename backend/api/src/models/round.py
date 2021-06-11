import datetime
from models.base_model import BaseModel
from models.place import Place
from mongoengine.fields import EmbeddedDocument, StringField

class Round(EmbeddedDocument):
    place=EmbeddedDocument(required=True)
    map_id=StringField(required=True)
