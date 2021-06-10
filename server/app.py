from flask import Flask, render_template, jsonify
from werkzeug.exceptions import HTTPException, NotFound
from pymongo import MongoClient

app = Flask(__name__)
mongo = MongoClient('mongodb://root:SGG@mongo:27017')

# '/<user>' route fetches a problem from an user's dataset, defaults to 'demo'
@app.route('/')
@app.route('/<user>')
def label(user='demo'):
    db = mongo[user]
    if db.list_collection_names() == []:
        raise NotFound("User not found.")
    ds = arbitrary(db['_datasets'])
    collection = ds['_id']
    instance = arbitrary(db[collection])
    return jsonify({'dataset': ds, 'instance': instance})

# Returns a random document from given collection
def arbitrary(coll):
    for x in coll.aggregate([{'$sample': { 'size': 1 }}]):
        return x

@app.errorhandler(Exception)
def error(e):
    code = 500
    msg = "Internal Server Error:\n" + str(e)
    if isinstance(e, HTTPException):
        code = e.code
        msg = e.description
    return render_template('error.html', code=code, message=msg)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080)
