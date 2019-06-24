import pymongo
from pymongo_conf import mycol, myclient # ne moramo da importujemo cijeli modul
'''
myclient.drop_database("mydatabase")

mylist = [
  { "name": "Amy", "address": {"name": "Apple st", "number": 652 }, "age": 35},
  { "name": "Hannah", "address": {"name": "Mountain", "number": 21}, "age": 42},
  { "name": "Michael", "address": {"name":  "Valley", "number": 345 }, "age": 37},
  { "name": "Sandy", "address": {"name":  "Ocean blvd", "number": 2 }, "age": 50},
  { "name": "Ana", "address": {"name":  "Valley", "number": 29 }, "age": 62}
]

x = mycol.insert_many(mylist)

x = mycol.find_one()

print(x)
print("-------")

for x in mycol.find():
  print(x)

print("-------")

# vraca sve dokumente bez _id kljuca
for x in mycol.find({},{ "_id": 0, "name": 1, "address": 1 }):
  print(x)

print("-------")
# vraca sve dokumente ali bez njihove adrese
for x in mycol.find({},{ "address": 0 }):
  print(x)
'''
print("-------")
# ERROR jer se komb 0 i 1
'''
for x in mycol.find({},{ "name": 1, "address": 0 }):
  print(x)
'''

# Queries

# I) Jednostavni upiti
# Naci korisnika/e cija je vrijednost name = "Amy"
dok = list(mycol.find({"name": "Amy"}))
print("---------")
print(dok)

# Naci korisnika/e cija je vrijednost address = "Valley" i vratiti samo name
dok2 = list(mycol.find({"address.name": "Valley"}, {"_id":0, "name": 1}))
print("---------")
print(dok2)

# Naci korisnike cije je ime Susan
dok3 = list(mycol.find({"name": "Susan"}))
print("---------")
print(dok3)
  
# Naci korisnika/e cije je ime Ana i adresa Valley 29
dok4 = list(mycol.find({"name":"Ana", "address.name":"Valley", "address.number": 29}))
print("---------")
print(dok4)

# II) like($regex), $gt(e), $ne, $eq, $lt(e), $in, $and, $or, ugnijezdeni objekti
# Naci sve korisnike cije ime pocinje sa A
dok5 = list(mycol.find({"name": {"$regex": "^A"}}))
print("---------")
print(dok5)
# Naci sve korisnike koji imaju vise od 40 godina
dok6 = mycol.find({"age": {"$gt": 40}})
print("---------")
print(list(dok6))
# Naci sve korisnike koji imaju vise od 30, a manje od 40 godina
dok7 = mycol.find({"age": {"$gt": 30, "$lt": 40}})
print("---------")
print(list(dok7))
# Naci sve korisnike koji imaju vise od 30 ili cije je ime Sandy
dok8 = mycol.find({"$or":[{"age": {"$gte": 51}}, {"name": "Sandy"}]})
print("---------")
print(list(dok8))
# Naci sve korisnike ciji je broj adrese 21
dok9 = mycol.find({"address.number": 21})
print("---------")
print(list(dok9))
# Naci sve korisnike cije ime pocinje sa A, a mladnji su od 50 godina (vrati samo ime)
dok10 = mycol.find({"name": {"$regex": "^A"}, "age": {"$lt": 50}}, {"_id": 0, "name": 1})
print("---------")
print(list(dok10))
# Naci sve korisnike cija vrijednost za age nije 35
dok11 = mycol.find({"age": {"$ne": 35}})
print("---------")
print(list(dok11))

# Hint1: db.customers.find( { $or: [ { age: { $lt: value } }, { name: value } ] } )
# Hint2: db.customers.find({ "address.name": { $regex: /N/ }}), ^ - starts with, $ - ends with
# Hint3: db.customers.find({ _id: { $in: [ 5, ObjectId("507c35dd8fada716c89d0013") ] } })



