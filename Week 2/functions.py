# Funkcije

def add_number(param1, param2):
    return param1 + param2

# print(add_number())
# print(add_number(1))
# print(add_number(1,2))

def print_country(country = "Crna Gora"):
  print("Ja sam iz " + country)

# print_country()

def print_food(food):
  for x in food:
    print(x)

# print_country("Italija")
# fruits = ["apple", "banana", "cherry"]
# print_food(fruits)

def ime_prezime(ime="Stevan", prezime="Čakić"):
    return f'{ime} {prezime}'

print(ime_prezime(prezime="Prezime", ime="Ime"))