import os
from flask import Flask
from flask import request, render_template, make_response, jsonify
from flask.ext import restful
from flask.ext.pymongo import PyMongo
from bson.json_util import dumps
from flask.ext.httpauth import HTTPBasicAuth
#from flask.ext.cors import CORS

MONGO_URI = os.environ.get('MONGOLAB_URI')
if not MONGO_URI:
    MONGO_URI = "mongodb://localhost:27017/rest";

app = Flask(__name__)
app.config['MONGO_URI'] = MONGO_URI
#app.config['CORS_HEADERS'] = 'Content-Type'

#cors = CORS(app)
mongo = PyMongo(app)

@app.after_request
def add_cors(resp):
    # Ensure all responses have the CORS headers. This ensures any failures are also accessible by the client.
    resp.headers['Access-Control-Allow-Origin'] = request.headers.get('Origin','*')
    resp.headers['Access-Control-Allow-Credentials'] = 'true'
    resp.headers['Access-Control-Allow-Methods'] = 'POST, OPTIONS, GET, PUT, DELETE'
    resp.headers['Access-Control-Allow-Headers'] = request.headers.get( 'Access-Control-Request-Headers', 'Authorization' )
    # set low for debugging
    if app.debug:
        resp.headers['Access-Control-Max-Age'] = '1'
    return resp
"""
"""

def output_json(obj, code, headers=None):
    resp = make_response(dumps(obj), code)
    resp.headers.extend(headers or {})
    return resp

DEFAULT_REPRESENTATIONS = {'application/json': output_json}
api = restful.Api(app)
api.representations = DEFAULT_REPRESENTATIONS


auth = HTTPBasicAuth()

@auth.get_password
def get_password(username):
    if username == 'miguel':
        return 'python'
    return None

@auth.error_handler
def unauthorized():
    return make_response(jsonify({'error': 'Unauthorized access'}), 401)
    
import resources