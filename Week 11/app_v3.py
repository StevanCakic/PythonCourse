from flask import Flask, request
from flask_restful import Resource, Api, reqparse
from bson.json_util import dumps
import pymongo
from flask_jwt import JWT, jwt_required
from security import identity, authenticate

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
#myclient.drop_database("mydatabase")
mydb = myclient["mydatabase"]
mycol = mydb["students"]

app = Flask(__name__)

app.secret_key = "neki_string_koji_ne_smije_da_bude_public" # Part of JWT

api = Api(app)

jwt = JWT(app, authenticate, identity) # /auth

class Student(Resource):
    @jwt_required()
    def get(self, name):
        try:
            student = list(mycol.find({"name": name}))
            if student:
                return dumps(student), 200
            else:
                return None, 404
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
    
    def delete(self, name):
        try:
            print(name)
            student = mycol.delete_one({"name": name})
            if student:
                return {"message": "Item deleted."}, 200
            else:
                return None, 404
        except Exception as e:
            return {"error": str(e)}, 400
    
    def put(self, name):
        
        try:
            '''
            parser = reqparse.RequestParser()
            parser.add_argument("name", type="string", required=False, help="This field cant be left blank.")
            parser.add_argument("email", type="string", required=False, help="This field cant be left blank.")
            parser.add_argument("index", type="string", required=False, help="This field cant be left blank.")
            
            # Pazite da parametre koje ovdje rucno ne dodate nece biti izdvojeni iz linka, npr. posaljete parametar another=1 => request_data["another"] -> KeyError
            request_data = parser.parse_args()
            '''
            request_data = request.get_json()
            student = list(mycol.find({"name": name}))
            new_student = {
                "name": request_data["name"],
                "email": request_data["email"],
                "index": request_data["index"]
            }
            
            if len(student) == 0:
                mycol.insert_one(new_student)
                return dumps(new_student), 201
            else:
                updated_student = mycol.update_one({"name": name}, {"$set": new_student})
                return {"message":"Updated"}, 200

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