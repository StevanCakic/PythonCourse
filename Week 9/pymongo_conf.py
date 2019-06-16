import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")
myclient.drop_database("mydatabase") # posle cemo govoriti o ovome
mydb = myclient["mydatabase"]
mycol = mydb["customers"]

