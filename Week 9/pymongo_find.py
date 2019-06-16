import pymongo
from pymongo_conf import mycol,myclient # ne moramo da importujemo cijeli modul

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

print("-------")
# ERROR jer se komb 0 i 1
'''
for x in mycol.find({},{ "name": 1, "address": 0 }):
  print(x)
'''

# Queries

# I) Jednostavni upiti
    # Odkomentarisati dio iz prethodnom primjera insert many
    # Naci korisnika/e cija je vrijednost name = "Amy"
    # Naci korisnika/e cija je vrijednost address = "Central st 954" i vratiti samo name
    # Naci korisnike cije je ime Susan
    # Naci korisnika/e cije je ime Susan i adresa One way 98  

# II) like($regex), $gt(e), $ne, $eq, $lt(e), $in, $and, $or, ugnijezdeni objekti
    # Naci sve korisnike cije ime pocinje sa A
    # Naci sve korisnike koji imaju vise od 40 godina
    # Naci sve korisnike koji imaju vise od 30, a manje od 40 godina
    # Naci sve korisnike koji imaju vise od 30 ili cije je ime Sandy
    # Naci sve korisnike ciji je broj adrese 21
    # Naci sve korisnike cije ime pocinje sa A, a mladnji su od 50 godina (vrati samo ime)
    # Naci sve korisnike cija vrijednost za age nije 35

    # Hint1: db.customers.find( { $or: [ { age: { $lt: value } }, { name: value } ] } )
    # Hint2: db.customers.find({ "address.name": { $regex: /N/ }}), ^ - starts with, $ - ends with
    # Hint3: db.customers.find({ _id: { $in: [ 5, ObjectId("507c35dd8fada716c89d0013") ] } })



