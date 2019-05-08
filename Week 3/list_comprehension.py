# List comprehension

# Napisati program koji kreira listu od 1-100, gdje su svi elementi kvadrirani:
# Koristici standardnu for petlju
# Izlaz: 1, 4, 9, 16, ..., 10000

# TODO

# Isti zadatak primjenom list comprehension
'''
squares = [i**2 for i in range(1, 101)]
print(squares)
'''

# Za listu kvadrata brojeva od 1 do 101 vratiti ostatke pri dijeljenju sa 5

'''
squares_mod5 = [i**2 % 5 for i in range(1, 101)]
print(squares_mod5)
'''

# Napisati program koji vraca sve filmove iz liste koji pocinju sa slovom T u novu listu
'''
movies = ['The Godfather', 'The Wizard of Oz', 'Citizen Kane', 
            'The Shawshank Redemption', 'Pulp Fiction']
# a) koristeci for loop
# TODO

# b) list comprehension
movies_start_with_the = [title for title in movies if title.startswith("T")]
print(movies_start_with_the)
'''

# Zakomplikujmo malo strukturu za movies

'''
movies = [('The Godfather', 1972), ('The Wizard of Oz', 1939), ('Citizen Kane', 1941), 
            ('The Shawshank Redemption', 1994), ('Pulp Fiction', 1994)]

# Izdvojite one filmove (samo title) koji su izasli nakon 1980 godine
movies_after1980 = [title for (title, year) in movies if year > 1980]
print(movies_after1980)
'''

# Probajte sami
'''
movies = [('The Godfather', 1972, "crime"), ('The Wizard of Oz', 1939, "drama"), 
            ('Citizen Kane', 1941, "drama"), ('The Shawshank Redemption', 1994, "drama"),
            ('Pulp Fiction', 1994, "triller")]
# TODO
'''
# Izdvojiti sve drama filmove (samo title) koji su snimljeni izmedju 1990 i 2000 godine

# Mnozenje vektora brojem
'''
vek = [1, 2, 3, -5]
print(vek * 3)

vek_mult3 = [num * 3 for num in vek]
print(vek_mult3)
'''

# Sami: Izdvojite sve parne brojeve iz segmenta 1 do 100 koristeci list comprehension
# TODO

# Sami: Za listu unijetih cijena, vratiti cijene bez PDV-a kao novu listu (PDV - 21%),
# koristiti list comprehension
# TODO

# Dekartov proizvod

'''
A = [1, 2, 3]
B = [4, 5, 2]

dekartov_prozvod = [(a,b) for a in A for b in B]
'''