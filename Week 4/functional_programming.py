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

f = build_quadratic_function(2, 3, -5)
print(f(0))
print(f(1))
print(f(2))

# Moze cak i ovako
print(build_quadratic_function(3, 2, 1)(2)) # 3*x*x + 2*x + 1 -> 3 * 2 * 2 + 2 * 2 + 1 = 17
