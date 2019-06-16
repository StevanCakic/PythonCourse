import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

# Kreiranje baze
mydb = myclient["mydatabase"]

print(mydb)

print(myclient.list_database_names())

# Prolazimo kroz sve baze
dblist = myclient.list_database_names()
if "mydatabase" in dblist:
    print("The database exists.")
else:
    print("DB is empty or not exists")

# Kreiranje kolekcije
mycollection = mydb["customers"]

collist = mydb.list_collection_names()
if "customers" in collist:
    print("The collection exists.")
else:
    print("Collection is empty or not exits")
