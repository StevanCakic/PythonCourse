import pymongo
from pymongo_conf import mycol, myclient

myquery = { "name": "Ana" }
newvalues = { "$set": { "age": 60 } }

mycol.update_one(myquery, newvalues)

#print "customers" after the update:
for x in mycol.find():
  print(x)

myquery = { "name": { "$regex": "^S" } }
newvalues = { "$set": { "address.name": "Mountain" } }

x = mycol.update_many(myquery, newvalues)

print(x.modified_count, "documents updated.")

