import pymongo
from pymongo_conf import mycol,myclient # ne moramo da importujemo cijeli modul

mylist = [
  { "name": "Amy", "address": {"name": "Apple st", "number": 652 }, "age": 35},
  { "name": "Hannah", "address": {"name": "Mountain", "number": 21}, "age": 42},
  { "name": "Michael", "address": {"name":  "Valley", "number": 345 }, "age": 37},
  { "name": "Sandy", "address": {"name":  "Ocean blvd", "number": 2 }, "age": 50},
  { "name": "Ana", "address": {"name":  "Valley", "number": 29 }, "age": 62}
]

x = mycol.insert_many(mylist)

# Sortira po kljucu name u opadajucem poretku, po default-u u rastucem
mydoc_sorted = mycol.find().sort("age", -1)
print(list(mydoc_sorted))
print("\n\n")

# Limit vraca n dokumenata (n argument za limit)
mydoc_limited = mycol.find().sort("age", -1).limit(3)
print(list(mydoc_limited))
print("\n\n")

# Skip prestakce prvih n dokumenata (n argument za limit)
mydoc_skiped = mycol.find().sort("age").limit(5).skip(2)
print(list(mydoc_skiped))
print("\n\n")

# Count vraca broj dokumenata koji zadovoljavaju odredjeni uslov
print(mydoc_skiped.count())

