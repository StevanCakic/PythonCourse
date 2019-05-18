# Drugi dio

# Zip 
'''
a = [1, 2, 3]
b = [4, 5, 6]

c = zip(a, b)
print(c)

for pair in zip(a, b):
    print(max(pair))

print(map(lambda pair: max(pair), zip(a,b)))


# Sta ako je jedna lista kraca od druge
a = [1, 2, 3]
b = [4, 5]

print(zip(a, b))
print(zip(b, a))
'''

# Dict zip
'''
dict_a = {"a": 1, "b": 2}
dict_b = {"a": 4, "b": 7}

print(zip(dict_a, dict_b))

# Zasto samo kljucevi?
# Ako se sjecate kad smo radili dict

for elem in dict_a:
    print(elem)

# Kako da uzmemo vridjednosti onda?

print(zip(dict_a, dict_b.values()))

def switch_key_value(d1, d2):
    dout = {}
    for d1key, d2val in zip(d1, d2.values()):
        dout[d1key] = d2val
    return dout

print(switch_key_value(dict_a, dict_b))
'''

# Enumerate 
'''
l = ["a", "b", "c"]

count = 0
for item in l:
    print(count, item)
    count += 1

for (count,item) in enumerate(l):
    print(count, item)

# Korisno u slucajevima kada nam je indeks bitan, npr. kad izvlacimo elemente sa parnih pozicija, do ili od odredjenog indeksa, itd
'''

# All i any
'''
l = [True, True, False, False]

print(all(l))
print(any(l))
'''

# Sort
'''
l = ["Petar", "Stefan", "Ivan", "Masa", "Andjela"]
print(l.sort())
print(l)
print(l.sort(reverse=True))
print(l)

# Sta bi se desilo kada bi probali da sortiramo toruku?

print(help(list.sort))

# 1AU - 149 597 871 kilometara
# format (name, radius, density, distance from Sun)
# Radius - u km
# Density - prosjecna gustina u g/cm^3
# Distance from Sun - Okvirna udaljenost planeta od Sunca, jedina AU

planets = [("Mercury", 2440, 5.43, 0.395), ("Venus", 6052, 5.24, 0.723),
            ("Earth", 6378, 5.52, 1.000), ("Mars", 3396, 3.93, 1530),
            ("Jupiter", 71492, 1.33, 5.210), ("Saturn", 60268, 0.69, 9.551),
            ("Uranus", 25559, 1.27, 19.213), ("Neptune", 24764, 1.64, 30.070)]

# Lista trenutno sortirana po rastojanju planeta od Sunca
# Sortirajmo listu planeta po velicinu (radius)

size = lambda planet: planet[1]
planets.sort(key=size, reverse=True)
print(planets)

# Kako ipak mozemo da sortiramo tuple, ali definitno kao output dobijamo novi
# jer smo rekli da je tuple immutable
print(help(sorted))

l_sorted = sorted(l)
print(l)
print(l_sorted)

print(sorted((17,2,5,3,1)))
print(sorted("Alfabet"))
'''