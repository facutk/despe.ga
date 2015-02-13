import os
from flask import Flask
from flask import render_template, make_response
from flask.ext import restful
from flask.ext.pymongo import PyMongo
from bson.json_util import dumps

MONGO_URI = os.environ.get('MONGOLAB_URI')
if not MONGO_URI:
    MONGO_URI = "mongodb://localhost:27017/rest";

app = Flask(__name__)
app.config['MONGO_URI'] = MONGO_URI
mongo = PyMongo(app)

def output_json(obj, code, headers=None):
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})
    return resp

DEFAULT_REPRESENTATIONS = {'application/json': output_json}
api = restful.Api(app)
api.representations = DEFAULT_REPRESENTATIONS

import resources