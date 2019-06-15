import functools

# Dekoratori, osnove

def my_decorator(func):
    @functools.wraps(func)
    def func_that_runs_func():
        print('Im decorator')
        func() # mozemo cak ovo da maknemo i na taj nacin da potpuno izmijenimo org funkciju
               # mada svakako da to i nema nekog smisla, zato ne zaboravljate da pozovete func()
        print("After decorator")
    return func_that_runs_func # ova funkcija ce da izmijeni org funkciju

@my_decorator
def my_func():
    print("I'm the function")

# my_func()


# Dekoratori sa argumentima

def decorator_with_arguments(number):
    def my_decorator(func):
        @functools.wraps(func)
        def func_that_runs_func(*args, **kwargs): # uvijek ako imate originalne func
                                                  # koje imaju parametre
            print('In the decorator')
            if number == 56:
                print("Do not run the function") 
            else:
                print("Run the function")   
                func(*args, **kwargs) # parametri originalne funkcije!
            print("After decorator")
        return func_that_runs_func
    return my_decorator


@decorator_with_arguments(56)
def my_func_too(a, b):
    print("Hello")
    print(a, b)
    print(a + b)

my_func_too(2, 20)

# vrlo korisnino, npr. umjesto 56 mozemo da proslijedimo user permission
# Npr. proslijedimo umjesto 56, user role i prikazemo/ne prikazemo neku stranicu korisniku
# Zamislite da imate puno admin stranica, bez dekorator u svakoj funkciji
# morali biste da pisete logiku i provjeravatate da li je user admin

# Takodje funkciju cesto imaju parametre, ali kako dekorator treba da radi
# sa funkcijama koje mogu da imaju razlicit broj argumenata, cesto se koriste args i kwargs