from mongoengine import (
    Document,
    StringField,
    ReferenceField,
    DictField,
)
from .dataset import Dataset


class Image(Document):
    dataset = ReferenceField(Dataset, required=True)
    url = StringField(required=True, unique_with="dataset")
    labels = DictField(StringField)
