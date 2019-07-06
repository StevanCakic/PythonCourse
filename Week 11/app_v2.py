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

class Student(Resource):

    def get(self, name):
        try:
            student = list(mycol.find({"name": name}))
            if student:
                return dumps(student), 200
            else:
                return None, 404
        except Exception as e:
            return {"error": str(e)}, 400

    def post(self, name): 
        try:
            # Ako dodamo force=True, nije neophodno da se salje Content-Type:"application/json"
            # Ako dodamo silent=True, vraca umjesto greske None (null)
            request_data = request.get_json() # ako ne setujemo u zahtjevu Content-Type:"application/json" ili posaljemo invalid JSON, greska
            new_student = {
                "name": request_data["name"],
                "email": request_data["email"],
                "index": request_data["index"]
            }
            mycol.insert_one(new_student)
            return dumps(new_student), 201
        except Exception as e:
            return {"error": str(e)}, 400

class StudentList(Resource):

    def get(self):
        try:
            students = list(mycol.find())
            if students:
                return dumps(students), 200
            else:
                return None, 404 
        except Exception as e:
            return dumps({"error": str(e)})

api.add_resource(Student, "/student/<string:name>")
api.add_resource(StudentList, "/students")

app.run(port=5000, debug=True)