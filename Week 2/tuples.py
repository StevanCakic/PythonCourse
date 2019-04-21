# Tuples

# Isrobati index i count metode
# Šta ako imamo tuple dužine 1
    # Šta je type(tuple) za ovakav primjer

# Isprobati da dodate, izmijenite ili obrišete element

# Sta se desava kada je duzina torke 1
# torka = (1)
# print(torka)

# Uporediti dir(tuple) i dir(list)


# Poredjenje velicina za list i tuple
'''
import sys
# print(dir(sys))

# Nas zanima sys.getsizeof

# print(help(sys.getsizeof))

lista = [1, 2, 3, "a", "b", "c", True, 2.73]
torka =  (1, 2, 3, "a", "b", "c", True, 2.73)

print(sys.getsizeof(lista))
print(sys.getsizeof(torka))
'''

# Mjerenje kreiranja listi i torki

'''
import timeit

# kreira 1000000 listi [1,2,3,4,5] i vrati koliko vremena je potrebno za izvrsavanje ovakvog koda
list_test = timeit.timeit(stmt="[1,2,3,4,5]", number=1000000)

# kreira 1000000 listi [1,2,3,4,5] i vrati koliko vremena je potrebno za izvrsavanje ovakvog koda
tuple_test = timeit.timeit(stmt="(1,2,3,4,5)", number=1000000)

print("List time: ", list_test)
print("Tuple time: ", tuple_test)
'''

# Tuple destructuring

# ime, prezime, godine = ("Stevan", "Čakić", 25)

# Ovo je moguce i za liste, isprobajte
# Sta ako je manje elemenata nego promjenjlivih, a sta ako ih je vise?