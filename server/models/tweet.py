from mongoengine import Document, StringField, ReferenceField, DictField, IntField
from .dataset import Dataset


class Tweet(Document):
    _id = IntField(primary_key=True)
    dataset = ReferenceField(Dataset, required=True)
    tweet = StringField(required=True)  # , unique_with="dataset")
    labels = DictField(StringField)
