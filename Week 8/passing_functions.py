def add_two_numbers():
    return 10 + 20

def function_caller(callback_function):
    return callback_function()

print(function_caller(add_two_numbers))

print(function_caller(lambda: 10 + 20))

# Sa lambda
print((lambda x: x * 3)(5))

# Standardna funkcija (isto kao gore)
def mult(x):
    return x * 3

print(mult(5))
