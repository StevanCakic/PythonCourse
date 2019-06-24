# Potrebno je koristiti modul pymongo
import pymongo

# Konektujte se na mongod server
myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Kreirati bazu cije je ime vjezbanje
myclient.drop_database("mydatabase")
mydb = myclient["mydatabase"]

# U njoj kreirati kolekciju users i setujemo validator za schemu
vv = {
      "$jsonSchema": {
          "bsonType": "object",
          "required": [ "name", "year"],
          "properties": {
            "name": {
               "bsonType": "string",
               "description": "must be a string and is required",
               "minLength": 4
            },
            "year": {
               "bsonType": "int",
               "description": "must be a number and is required",
               "minimum": 2017,
               "maximum": 3017,
            }
          }
      }
    }
mycol = mydb.create_collection("users", validator=vv)

# Svaki user je opisan sledecim atributima:
#   name - String required
#   year - Number required 

try:
    mydict1 = { "name": "John", "year": 3017 }
    doc1 = mycol.insert_one(mydict1)

except Exception as e:
    print(e)