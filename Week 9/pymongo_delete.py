import pymongo
from pymongo_conf import mycol,myclient # ne moramo da importujemo cijeli modul

myquery = { "name": "Amy" }

mycol.delete_one(myquery)

# Brise sve dokumente kod kojih vrijedost dokumenta za name pocinje slovom S
myquery = { "name": {"$regex": "^S"} }

x = mycol.delete_many(myquery)

print(x.deleted_count, " documents deleted.")

# Brise sve dokumente iz kolekcije mycol
x = mycol.delete_many({})

print(x.deleted_count, " documents deleted.")

# Brisanje kolekcije

mycol.drop()

