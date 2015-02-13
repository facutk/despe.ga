import json
from flask import abort, render_template, request
from flask.ext import restful
from app import app, api, mongo, auth
from bson.objectid import ObjectId

class ReadingList(restful.Resource):
    def __init__(self, *args, **kwargs):
        super(ReadingList, self).__init__()

    def get(self):
        return  [x for x in mongo.db.readings.find()]

    def post(self):
        reading = request.json
        reading_id =  mongo.db.readings.insert(reading)
        return mongo.db.readings.find_one({"_id": reading_id})
        #args = self.parser.parse_args()
        #if not args['reading']:
        #    abort(400)

        #jo = json.loads(args['reading'])



class Reading(restful.Resource):
    def get(self, reading_id):
        return mongo.db.readings.find_one_or_404({"_id": reading_id})

    def delete(self, reading_id):
        mongo.db.readings.find_one_or_404({"_id": reading_id})
        mongo.db.readings.remove({"_id": reading_id})
        return '', 204


class Root(restful.Resource):
    method_decorators = [auth.login_required]
    def get(self):
        return {
            'status': 'OK',
            'mongo': str(mongo.db),
        }

api.add_resource(Root, '/x')
api.add_resource(ReadingList, '/readings')
api.add_resource(Reading, '/readings/<ObjectId:reading_id>')


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/saludo')
def saludo():
    return 'Hola'
    
@app.route('/secret')
@auth.login_required
def secret():
    return "Hello, %s!" % auth.username()