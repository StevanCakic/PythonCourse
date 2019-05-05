# Dictionaries

# Prvi dio
# Kreirajmo dictionary koji sadrži različite tipove podataka
# Isprobajmo indeksiranje

# Drugi dio

# dict_proizvod1 = {"id":1, "ime": "Laptop", "marka": "Dell", "cijena": 500, "valuta": "eur", "opis":"i5, 8GB RAM, 256GB SSD" }
# dict_proizvod2 = {"id": 2, "ime": "Tastatura", "marka": "Dell", "cijena": 20.5, "valuta": "eur"}

# Izlistati kljuceve oba rjecnika
# Izlistati vrijednosti oba rjecnika
# Izlistati par (kljuc, vrijednost)
# Za sve prozvode provjeriti da li imaju kljuc "opis". Ako imaju ne mijenjati ga, a ako nemaju
# dodati vrijednost kljuca opis na "Default opis"

# Kreirajmo dict_a, pa nakon toga i dict_b u koji zelimo da sacuvamo dict_a.
# Sta ce se desiti ako promijenimo vrijednost nekog kljuca u dict_b?

# Da li je moguce da dictionary sadrzi dictionary?

# Treci dio

# fromkeys

'''
key1, key2, value = "key1", "key2", 2
dict_a = {"a": 1, "b":2}
dict_b = {}
print(dict_b.fromkeys((key1, key2), value))
'''
# check if key in dict

'''
if "a" in dict_a:
    print("Dict a sadrzi kljuc a")
else:
    print("Dict a ne sadrzi kluc a")
'''
# Using get

'''
print(dict_b.get("key1", "Vrijednost"))
print(dict_b) # Prazno? Zasto?
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