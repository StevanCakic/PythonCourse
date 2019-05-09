# Scope

# Primjer 1
# Local
'''
def fun():
    x = 3
    return x

lambda_exp = lambda x: x * x

# Enclosing function

name = "Ivan"

def a():
    # Enclosing function
    name = "Marko"
    def b():
        print("Zdravo ", name)
    b()

a()

# Global

print(name)
'''

# Primjer 2
'''
x = 50
def func(x):
    print("x je: ",x)
    x = 2
    print("izmijenjeno x: ", x)

func(x)
print("x van funkcije je: ", x)
'''

# Primjer 3
'''
x = 50
def func():
    global x
    print("x je: ", x)
    x = 2
    print("izmijenjeno x: ", x)

print("x prije poziva funkcije: ", x)
func()
print("x van funkcije je: ", x)
'''