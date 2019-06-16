import pymongo
import pymongo_conf
# Insert one document

mydict1 = { "name": "John", "address": "Highway 37" }

doc1 = pymongo_conf.mycol.insert_one(mydict1)

mydict2 = { "name": "Peter", "address": "Lowstreet 27" }

doc2 = pymongo_conf.mycol.insert_one(mydict2)

print(doc2.inserted_id)

# Insert many documents

'''
pymongo_conf.myclient.drop_database("mydatabase") # ispraznimo bazu
mylist = [
  { "name": "Amy", "address": "Apple st 652"},
  { "name": "Hannah", "address": "Mountain 21"},
  { "name": "Michael", "address": "Valley 345"},
  { "name": "Sandy", "address": "Ocean blvd 2"},
  { "name": "Betty", "address": "Green Grass 1"},
  { "name": "Richard", "address": "Sky st 331"},
  { "name": "Susan", "address": "One way 98"},
  { "name": "Vicky", "address": "Yellow Garden 2"},
  { "name": "Ben", "address": "Park Lane 38"},
  { "name": "William", "address": "Central st 954"},
  { "name": "Chuck", "address": "Main Road 989"},
  { "name": "Viola", "address": "Sideway 1633"},
  { "name": "Susan", "address": "One way 10"}
]

x = pymongo_conf.mycol.insert_many(mylist)

#print list of the _id values of the inserted documents:
print(x.inserted_ids)

'''
# Sta je _id