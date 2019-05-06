# Fajlovi

# Prvi dio (read i seek)
'''
f = open("./files/file.txt")
print(f.read())
print(f.read())

# Zasto kad opet pozovemo read() ne stampa nista?

f.seek(0)
print(f.read())

f.seek(0)
print(f.readlines())

f.seek(0)
# Iteracija kroz fajl liniju po liniju
for line in f:
    print(line)

f.close() # zatvaranje fajla
'''

# Drugi dio (write, append i close)
'''
f = open("./files/demofile2.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("./files/demofile2.txt", "r")
print(f.read())

f = open("./files/demofile.txt", "w")
f.write("Woops! I have deleted the content!")
f.close()

#open and read the file after the appending:
f = open("demofile3.txt", "r")
print(f.read())
f.close()

'''

# Kratko o with

'''
with open("./files/file.txt") as f:
    data = f.read()
    print(data)
'''

# Brisanje fajlova i foldera

'''
import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist")

import os
os.rmdir("myfolder") # za brisanje foldera

'''

# Zadatak: 
# Potrebno je izdvojiti/prikazati sve filmove cija je ocjena veca od unijete i 
# ciji je zanr filma odgovara unijetom zanru.

# Korisniku pri unosi napomenutu da su ocjene od 1 do 10, a osim toga
# treba napomenuti i koje zanrove moze da odabere.
# Ako korisnik unese podatke pogresno, treba da mi se prikaze greska i da mu se napomene
# da opet unosi novi input

# Napomena: Kreirati fajl filmovi.txt u kome se svaki film, pojedinacno, cuva u jednom redom,
# tj. ako imate unos od 5 filmova, fajl treba da sadrzi 5 linija. 
# Takodje, svaki film je opisan: nazivom, ocjenom, godina izlaska i zanrom
    # Atributi filma odvojeni su sa ;
    # Ocjene su zaokruzeni float brojevi (od 1 do 10) na dvije decimale
    # Film moze da ima vise od jednog zanra, zanrovi su razdvojeni zarezima 

# Preporuka, koristiti list comprehension, funkcija za konverziju stringa u torku je tuple
# Hint: tup = tuple(some_str.split(",")) - konvertuje npr. "abcd,abbccd" -> ("abcd","abbccd")