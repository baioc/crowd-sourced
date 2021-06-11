from mongoengine import (
    Document,
    StringField,
    ReferenceField,
    DictField,
)
from .dataset import Dataset


class Instance(Document):
    dataset = ReferenceField(Dataset, required=True)
    url = StringField(required=True, unique_with="dataset")
    labels = DictField()  # label -> frequency
    text = StringField(required=True)
    text_url = StringField(required=True)
