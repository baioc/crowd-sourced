from mongoengine import (
    Document,
    StringField,
    ListField,
)


class Dataset(Document):
    name = StringField(primary_key=True)
    content_type = StringField(required=True, choices=["IMAGE", "TEXT"])
    message = StringField(required=True)
    label_type = StringField(required=True, choices=["CLASS", "LABEL", "GRID"])
    options = ListField(StringField())
