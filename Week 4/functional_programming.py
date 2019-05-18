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

# TODO Kako ovo da prepravimo?
# Kod Python2 ovo radi ocekivano
print(even_elems)
'''

# Map - x1, x2, x3, ..., xN => f(x1), f(x2), .... , f(xN) 
# Pretpostavimo da imamo listu gradova sa trenitnim temperaturama u C

'''
city_temp_c = [("Podgorica", 20), ("Niksic", 15), ("Budva", 18), ("Cetinje", 16), ("Bijelo Polje", 11), ("Pljevlja", 12)]

# Potrebno je da vratimo listu torki (grad, temp_F) 
# Formula za konverziju iz C u F -> 9/5 * C + 32 
city_temp_f = map(lambda elem: (elem[0], (9 / 5) * elem[1] + 32), city_temp_c)
print(list(city_temp_f))
'''

# Sabiranje elemenata iz dvije razlicite liste
'''
a = [1, 2, 3]
b = [4, 5, 6]

sum_lists = map(lambda x, y: x + y, a, b)
print(list(sum_lists))
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