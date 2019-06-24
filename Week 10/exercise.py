# Potrebno je koristiti modul pymongo
import pymongo
# Konektujte se na mongod server
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# Kreirati bazu cije je ime vjezbanje
mydb = myclient["vjezbanje"]
# U njoj kreirati kolekciju users
mycol = mydb.create_collection("users", {
   "validator": {
      "$jsonSchema": {
          "bsonType": "object",
          "required": [ "name", "year" ]
      }
    }})
# Svaki user je opisan sledecim atributima:
#   name - String
#    

mydict1 = { "name": "John", "year": "37" }

doc1 = mycol.insert_one(mydict1)