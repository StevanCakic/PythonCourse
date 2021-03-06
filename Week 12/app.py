from flask import Flask, request, jsonify
from flask_restful import Resource, Api, reqparse
from bson.json_util import dumps
import pymongo
from flask_jwt import JWT, jwt_required
from security import identity, authenticate
import json

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# myclient.drop_database("mydatabase")
mydb = myclient["mydatabase"]
vv = {
      "$jsonSchema": {
          "bsonType": "object",
          "required": [ "name", "email", "index"],
          "properties": {
            "name": {
               "bsonType": "string",
               "description": "must be a string and is required",
               "minLength": 4
            },
            "email": {
               "bsonType": "string",
               "description": "must be a number and is required"
            },
            "index": {
               "bsonType": "string",
               "description": "must be a number and is required"
            }
          }
      }
    }

if not "students" in mydb.list_collection_names():
    mycol = mydb.create_collection("students", validator=vv)
    mycol.create_index("index", unique=True)
else:
    mycol = mydb["students"]

app = Flask(__name__)

app.secret_key = "neki_string_koji_ne_smije_da_bude_public" # Part of JWT

api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

class Student(Resource):
    
    def get(self, name):
        try:
            student = list(mycol.find({"name": name}))
            if student:
                return dumps(student), 200
            else:
                return {"message": "Student with this name not found."}, 404
        except Exception as e:
            return {"error": str(e)}, 400

    @jwt_required()
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
    
    @jwt_required()
    def delete(self, name):
        try:
            student = mycol.find_one_and_delete({"name": name})
            if student:
                return {"message": "Student deleted."}, 200
            else:
                return {"message": "Student with this name not found."}, 404
        except Exception as e:
            return {"error": str(e)}, 400
    
    @jwt_required()
    def put(self, name):
        try:
            '''
            request_data = request.get_json()'''
            student = list(mycol.find({"name": name}))
            parser = reqparse.RequestParser()
            is_required = False
            if not student: # ako ne postoji
                is_required = True
            else:
                student = student[0]
            parser.add_argument("name", type=str, required=is_required)
            parser.add_argument("email", type=str, required=is_required)
            parser.add_argument("index", type=str, required=is_required)
            # Pazite da parametre koje ovdje rucno ne dodate nece biti izdvojeni iz linka, npr. posaljete parametar another=1 => request_data["another"] -> KeyError
            request_data = parser.parse_args()
            
            new_student = {
                "name":request_data["name"] if request_data["name"] else student["name"] ,
                "email": request_data["email"] if request_data["email"] else student["email"],
                "index": request_data["index"] if request_data["index"] else student["index"]
            }
            
            if not student:
                mycol.insert_one(new_student)
                return dumps(new_student), 201
            else:
                mycol.update_one({"name": name}, {"$set": new_student})
                return {"message": "Updated"}, 200

        except Exception as e:
            return {"error": str(e)}, 400

class StudentList(Resource):
    def get(self):
        try:
            students = list(mycol.find())
            if students:
                return dumps(students), 200
            else:
                return {"message": "No students found."}, 404
        except Exception as e:
            return dumps({"error": str(e)})

api.add_resource(Student, "/student/<string:name>")
api.add_resource(StudentList, "/students")

app.run(port=5000, debug=True)