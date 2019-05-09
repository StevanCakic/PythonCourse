# Functional programming

# Prvi dio
# Lambda expression

def square(a):
    return a*a

def square_short(a): return a * a

square_lambda = lambda a: a * a

# Sta ako je ne sacuvamo u varijablu?

# Malo tezi primjer
# f = a * x * x + b * x + c
def build_quadratic_function(a, b, c):
    return lambda x: a * x * x + b * x + c

'''
f = build_quadratic_function(2, 3, -5)
print(f(0))
print(f(1))
print(f(2))

# Moze cak i ovako
print(build_quadratic_function(3, 2, 1)(2)) # 3*x*x + 2*x + 1 -> 3 * 2 * 2 + 2 * 2 + 1 = 17

'''

# Drugi dio 

# Filter - x1, x2, x3, ..., xN => x?, x?, ..., x? (? - neki indeksi od 1 do N ali ne znamo unaprijed koji)
'''
def even_check(num):
    if num % 2 == 0:
        return True
    else:
        return False

# Lambda funkcija za prethodni primjer
even_check_lambda = lambda num: num % 2 == 0

even_check_lambda(14)

l = list(range(10))

even_elems = filter(even_check_lambda, l)

print(even_elems)
'''

# Map - x1, x2, x3, ..., xN => f(x1), f(x2), .... , f(xN) 
# Pretpostavimo da imamo listu gradova sa trenitnim temperaturama u C

'''
city_temp_c = [("Podgorica", 20), ("Niksic", 15), ("Budva", 18), ("Cetinje", 16), ("Bijelo Polje", 11), ("Pljevlja", 12)]

# Potrebno je da vratimo listu torki (grad, temp_F) 
# Formula za konverziju iz C u F -> 9/5 * C + 32 
city_temp_f = map(lambda elem: (elem[0], (9 / 5) * elem[1] + 32), city_temp_c)
print(city_temp_f)
'''

# Sabiranje elemenata iz dvije razlicite liste
'''
a = [1, 2, 3]
b = [4, 5, 6]

sum_lists = map(lambda x, y: x + y, a, b)
print(sum_lists)
'''

# Reduce - x1, x2, x3, ..., xN => f( f( f(x1, x2), x3), ...., xN)
# 1) val1 = f(x1, x2)
# 2) val2 = f(val1, x3)
# ....
# N) return val(N-1)

'''
from functools import reduce


a = [1, 2, 3, 4]
suma = reduce(lambda x, y: x + y, a)

# Kako smo dobili ovo? Nacrtajmo semu

print(suma)

b = [-5, 10, 2, 7]
max_num = reduce(lambda x, y: x if x > y else y, b)
# Postoji i ugradjena funkcija max
'''

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