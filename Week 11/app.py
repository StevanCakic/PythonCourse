from flask import Flask, jsonify, request
import pymongo
from bson.json_util import dumps

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myclient.drop_database("mydatabase") # posle cemo govoriti o ovome
mydb = myclient["mydatabase"]
mycol = mydb["users"]

# create the little application object
app = Flask(__name__)

# U slucaju kada pricamo o serveru
# POST - used to receive data
# GET - send data back only

# U slucaju da je browser 
# POST - used to send data
# GET - used to receive data

# Mi sada radimo serverski dio

# POST /user, data: {name:, email:} - kreira korisnika sa dva atributa, name i email
@app.route("/user", methods=["POST"])
def create_user():
    request_data = request.get_json()
    try:
        new_store = {
            "name": request_data["name"],
            "email": request_data["email"]
        }
        mycol.insert_one(new_store)
        return dumps(new_store)
    except Exception as e:
        return jsonify({"error": str(e)})
    

# GET /user/<string:name> - vraca usera po username-u
@app.route("/user/<string:name>") # http://127.0.0.1:5000/user/some_username
def get_user(name):
    try:
        user = list(mycol.find({"name": name}))
        return dumps(user)
    except Exception as e:
        return jsonify({"error": str(e)})

# GET /users - vraca sve usere
@app.route("/users")
def get_users():
    try:
        users = list(mycol.find())
        return dumps(users)
    except Exception as e:
        return jsonify({"error": str(e)})

app.run(port=5000)