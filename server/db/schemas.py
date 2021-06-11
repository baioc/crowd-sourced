from mongoengine import (
    Document,
    StringField,
    IntField,
    ListField,
    ReferenceField,
    DictField
)

class Dataset(Document):
    name = StringField(primary_key=True)
    content_type = StringField(required=True, choices=["IMAGE", "TEXT"])
    message = StringField(required=True)
    label_type = StringField(required=True, choices=["CLASS", "LABEL", "GRID"])
    options = ListField(StringField())

class Image(Document):
    dataset = ReferenceField(Dataset, required=True)
    url = StringField(required=True, unique_with="dataset")
    labels = DictField(StringField)

class Tweet(Document):
    _id = IntField(primary_key=True)
    dataset = ReferenceField(Dataset, required=True)
    tweet = StringField(required=True) #, unique_with="dataset")
    labels = DictField(StringField)

class Instance(Document):
    dataset = ReferenceField(Dataset, required=True)
    url = StringField(required=True, unique_with="dataset")
    labels = DictField()  # label -> frequency
    text = StringField(required=True)
    text_url = StringField(required=True)