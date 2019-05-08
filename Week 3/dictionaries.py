# Dictionaries

# Prvi dio
# Kreirajmo dictionary koji sadrži različite tipove podataka
# Isprobajmo indeksiranje
'''
my_dict = {"ime": "Marko", "prezime": "Markovic", "godine": 30}

# print(my_dict)
# my_dict["ime"] = "Ivan"
# print(my_dict)
# print(my_dict["adresa"])

my_dict1 = dict(my_dict)
my_dict1["ime"] = "Jovan"
print(my_dict)
print(my_dict1)
'''

# Drugi dio

dict_proizvod1 = {"id":1, "ime": "Laptop", "marka": "Dell", "cijena": 500, "valuta": "eur", "opis":"i5, 8GB RAM, 256GB SSD" }
dict_proizvod2 = {"id": 2, "ime": "Tastatura", "marka": "Dell", "cijena": 20.5, "valuta": "eur"}

# Izlistati kljuceve oba rjecnika
'''
print(dict_proizvod1.keys())
print(dict_proizvod2.keys())

# Izlistati vrijednosti oba rjecnika
print(dict_proizvod1.values())
print(dict_proizvod2.values())

# Izlistati par (kljuc, vrijednost)
print(dict_proizvod1.items())
print(dict_proizvod2.items())
'''

# Za sve prozvode provjeriti da li imaju kljuc "opis". Ako imaju ne mijenjati mu vrijednost, a ako nemaju
# dodati vrijednost kljuca opis na "Default opis"
'''
has_key = False

for key in dict_proizvod2.keys():
  if key == "opis":
    has_key = True
    break

# print(dict_proizvod2["opis"])

if not has_key:
  dict_proizvod2["opis"] = "vrijednost"

print(dict_proizvod2)
'''

# Da li je moguce da dictionary sadrzi dictionary?

# dict_proizvod3 = {"proizvod1": dict_proizvod1, "proizvod2": dict_proizvod2}
# print(dict_proizvod3)

# Treci dio

# fromkeys

'''
key1, key2, value = "key1", "key2", 2
dict_a = {"a": 1, "b":2}
dict_b = {}
print(dict_b.fromkeys((key1, key2), value))
'''
# check if key in dict

dict_a = {"a": 1, "b": 2}
'''
if "a" in dict_a:
    print("Dict a sadrzi kljuc a")
else:
    print("Dict a ne sadrzi kluc a")
'''
# Using get
'''
print(dict_a.get("key1", "Vrijednost"))
print(dict_a) # Prazno? Zasto?
'''
# fromkeys
'''
dict_b = dict(dict_b.fromkeys((key1, key2), value))
print(dict_b) 
'''
# update 
'''
car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

car.update({"color": "White"})
print(car)

'''

# Iteracija kroz dict (keys, values, items)
'''
dict_a = {"a": 1, "b": 2, "c": "Hi"}

for key in dict_a.keys():
    print(key)

for value in dict_a.values():
    print(value)

for key, value in dict_a.items():
    print(key, "=", value)
'''