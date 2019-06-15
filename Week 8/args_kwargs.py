def my_fun(arg1, arg2):
    return arg1 + arg2

print(my_fun(2, 3))

def my_long_fun(arg1, arg2, arg3, arg4, arg5):
    return arg1 + arg2 + arg3 + arg4 + arg5

def my_list_addition(lista):
    return sum(lista)

# Problem sto moramo da znamo tacan broj argumenata
print(my_long_fun(1,2,3,4,5))

# Problem sto moramo da proslijedimo listu
print(my_list_addition([1,2,3,4,5]))

# Postoji rjesenje

def addition_simplified(*args):
    return sum(args)

print(addition_simplified(1,2,3))

def what_are_kwargs(*args, **kwargs):
    print(args)
    print(*args)
    print(type(args))
    print(kwargs)
    print(type(kwargs))

what_are_kwargs(10, 20, 30, name="Marko", surname="Markovic")

# Sta ako uklonimo name i surname?

# Naravno, ako znamo koliko imamo parametara i njihov redosled ne moramo da koristimo 
# args i/ili kwargs


def test_args_kwargs(arg1, arg2, arg3):
    print("arg1:", arg1)
    print("arg2:", arg2)
    print("arg3:", arg3)

# sa *args
args = ("two", 3,5)
test_args_kwargs(*args)


# sa **kwargs:
kwargs = {"arg3": 3, "arg2": "two","arg1":5}
test_args_kwargs(**kwargs)