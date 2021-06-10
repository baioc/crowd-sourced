"""This module contains the logic for the main Flask API"""

from flask import Flask, render_template, jsonify
from werkzeug.exceptions import HTTPException, NotFound
from pymongo import MongoClient

app = Flask(__name__)
mongo = MongoClient("mongodb://root:SGG@mongo:27017")


@app.route("/")
@app.route("/<user>")
def label(user="demo"):
    """
    - Returns a JSON data of the results to the frontend
    on the routes of / and /<user>
    - '/<user>' route fetches a problem from an user's
    dataset, defaults to 'demo'

    Parameters:
        user='demo' (str): User to obtain record for

    Returns:
        JSON(JSON): A JSON format of the data
    """
    database = mongo[user]
    if database.list_collection_names() == []:
        raise NotFound("User not found.")
    datasets = arbitrary(database["_datasets"])
    collection = datasets["_id"]
    instance = arbitrary(database[collection])
    return jsonify({"dataset": datasets, "instance": instance})


def arbitrary(coll):
    """
    Returns a random document from given collection

    Parameters:
        coll (MongoDB Object): An object used to represent a
    class object from the MongoDB

    Returns:
        entry: A random entry selected from an aggregation of the
    data
    """
    for entry in coll.aggregate([{"$sample": {"size": 1}}]):
        return entry


@app.errorhandler(Exception)
def error(error_object):
    """
    Responsible for error handling, if any, within the
    routing mechanism

    Parameters:
        error (Exception): An exception object to describe
    the error itself

    Returns:
        JSON(JSON): Returns an error page for the
    invalid request
    """
    code = 500
    msg = "Internal Server Error:\n" + str(error_object)
    if isinstance(error_object, HTTPException):
        code = error_object.code
        msg = error_object.description
    return render_template("error.html", code=code, message=msg)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
