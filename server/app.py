"""This module contains the backend logic for the Flask API"""

from flask import Flask, render_template, jsonify, request, Response
from werkzeug.exceptions import HTTPException
from mongoengine import connect

# Local imports
from .models.instance import Instance
from .models.dataset import Dataset

app = Flask(__name__)
connect(host="mongodb://root:SGG@mongo:27017/demo?authSource=admin")


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
        if not answer_is_valid(dataset_id, instance_id, label):
            raise HTTPException(response=Response(status=400))

        instance = Instance.objects(dataset=dataset_id, url=instance_id).get()
        labels = instance["labels"]
        frequency = labels[label] + 1 if label in labels else 1
        labels[label] = frequency
        instance.save()

        return Response(status=201)


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


def answer_is_valid(dataset_id, instance_id, answer):
    """
    Checks whether an answer to a labelling problem is valid.

    Parameters:
        answer (JSON): Answer object containing dataset and instances id, as
                       well as the answered label itself

    Returns:
        ok (Boolean): Whether the answer is valid or not
    """

    if not dataset_id or not instance_id or not answer:  # all required
        return False

    instance = Instance.objects(dataset=dataset_id, url=instance_id).first()
    if instance is None:
        return False

    dataset = Dataset.objects(name=dataset_id).get()
    type = dataset["label_type"]
    options = dataset["options"]
    if type not in ["CLASS", "LABEL", "GRID"]:
        return False
    elif type == "CLASS" and answer not in options:
        return False
    elif type == "LABEL" and answer.trim() == "":
        return False  # XXX: we could apply some regex for text validation
    elif type == "GRID":
        # TODO: 'GRID' answer should be a collection of selections
        raise HTTPException(response=Response(status=501))  # "not implemented"

    return True


@app.errorhandler(Exception)
def error(err):
    """
    Handles any errors (standard HTTP and Python exceptions) in the server.

    Parameters:
        err (Exception): An exception object representing the error itself

    Returns:
        (HTML): Error page for the user to see
    """

    code = 500  # default
    msg = "Internal Server Error:\n" + str(err)
    if isinstance(err, HTTPException):
        code = err.code
        msg = err.description

    return render_template("error.html", code=code, message=msg), code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
