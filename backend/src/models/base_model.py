from mongoengine import Document
from mongoengine.fields import DateTimeField
import datetime

class BaseModel(Document):
    updated_at = DateTimeField(default=datetime.datetime.utcnow)

    meta = {'allow_inheritance': True}


