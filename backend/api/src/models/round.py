import datetime
from models.base_model import BaseModel
from models.place import Place
from mongoengine.fields import EmbeddedDocument, StringField, EmbeddedDocumentField

class Round(EmbeddedDocument):
    place=EmbeddedDocumentField(required=True, document_type=Place)
    map_id=StringField(required=True)
