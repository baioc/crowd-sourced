"""This module contains the backend logic for the Flask API"""

from flask import Flask, render_template, jsonify, request, Response
from werkzeug.exceptions import HTTPException
from mongoengine import (
    connect,
    Document,
    StringField,
    ListField,
    ReferenceField,
    DictField,
    IntField,
    DoesNotExist
)

app = Flask(__name__)
connect(host="mongodb://root:SGG@mongo:27017/demo?authSource=admin")


class Dataset(Document):
    name = StringField(primary_key=True)
    content_type = StringField(required=True, choices=["IMAGE", "TEXT"])
    message = StringField(required=True)
    label_type = StringField(required=True, choices=["CLASS", "LABEL", "GRID"])
    options = ListField(StringField())


class Instance(Document):
    dataset = ReferenceField(Dataset, required=True)
    url = StringField(required=True, unique_with="dataset")
    labels = DictField(IntField())


@app.route("/", methods=["GET", "POST"])
def index():
    """GETs a random labelling problem from one of the registered datasets, or
    processes an answer being POSTed back by a client."""

    if request.method == "GET":
        instance = arbitrary(Instance.objects)
        dataset = Dataset.objects(name=instance["dataset"]).get()
        return jsonify(
            {
                "dataset": dataset.to_mongo(),
                "instance": {"_id": instance["url"]},
            }
        )

    elif request.method == "POST":
        answer = request.get_json()
        dataset_id = answer.get("dataset_id")
        instance_id = answer.get("instance_id")
        label = answer.get("label")
        frequency = -1
        try:
            doc = Instance.objects(dataset=dataset_id, url=instance_id).get()
            labels = doc["labels"]
            frequency = labels[label] + 1 if label in labels else 0
            labels[label] = frequency
            doc.save()
        except DoesNotExist:
            pass  # TODO: query argument validation
        return jsonify(
            {
                "dataset_id": dataset_id,
                "instance_id": instance_id,
                "label": label,
                "frequency": frequency,
            }
        )


def arbitrary(coll):
    """
    Returns an arbitrary item from a given collection.

    Parameters:
        coll (Collection): Object representing a queryable MongoDB Collection

    Returns:
        entry: A random entry selected from an aggregation of the data
    """

    for entry in coll.aggregate([{"$sample": {"size": 1}}]):
        return entry


@app.errorhandler(Exception)
def error(err):
    """
    Handles any errors (HTTP and Python) in the server.

    Parameters:
        err (Exception): An exception object representing the error itself

    Returns:
        JSON(JSON): Returns an error page for the invalid request
    """

    code = 500
    msg = "Internal Server Error:\n" + str(err)
    if isinstance(err, HTTPException):
        code = err.code
        msg = err.description

    return render_template("error.html", code=code, message=msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
