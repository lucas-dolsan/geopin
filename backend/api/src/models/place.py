from models.base_model import BaseModel
from mongoengine.document import EmbeddedDocument

from mongoengine.fields import PointField

class Place(EmbeddedDocument):
    location=PointField()

