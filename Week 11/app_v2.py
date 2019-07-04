from flask import Flask, request
from flask_restful import Resource, Api
from bson.json_util import dumps
import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myclient.drop_database("mydatabase")
mydb = myclient["mydatabase"]
mycol = mydb["users"]

app = Flask(__name__)
api = Api(app)

class User(Resource):

    def get(self, name):
        try:
            user = list(mycol.find({"name": name}))
            if user:
                return user, 200
            else:
                return None, 404
        except Exception as e:
            return {"error": str(e)}, 400

    def post(self): 
        try:
            # Ako dodamo force=True, nije neophodno da se salje Content-Type:"application/json"
            # Ako dodamo silent=True, vraca umjesto greske None (null)
            request_data = request.get_json() # ako ne setujemo u zahtjevu Content-Type:"application/json" ili posaljemo invalid JSON, greska
            new_user = {
                "name": request_data["name"],
                "email": request_data["email"]
            }
            mycol.insert_one(new_user)
            return new_user, 201
        except Exception as e:
            return {"error": str(e)}, 400

class UserList(Resource):

    def get(self):
        try:
            users = list(mycol.find())
            if users:
                return users, 200
            else:
                return None, 404 
        except Exception as e:
            return dumps({"error": str(e)})

api.add_resource(User, "/user/<string:name>", "/user")
api.add_resource(UserList, "/users")

app.run(port=5000, debug=True)