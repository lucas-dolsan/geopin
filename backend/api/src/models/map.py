
import datetime
from models.base_model import BaseModel
from models.place import Place

from mongoengine.fields import EmbeddedDocumentListField, StringField

class Map(BaseModel):
    name=StringField(required=True)
    places=EmbeddedDocumentListField(document_type=Place)
