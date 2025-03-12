def dijeljenje():
    try:
        x = int(input("Unesite broj: "))
        rezultat = 10 / x
        print(f"Rezultat: {rezultat}")
    except ZeroDivisionError:
        print("Greška: Dijeljenje sa nulom nije dozvoljeno!")

def citanje_fajla():
    try:
        with open("nepostojeci_fajl.txt", "r") as fajl:
            sadrzaj = fajl.read()
            print(sadrzaj)
    except FileNotFoundError:
        print("Greška: Fajl ne postoji!")

def unos_broja():
    try:
        broj = int(input("Unesite broj: "))
        print(f"Uneli ste broj: {broj}")
    except ValueError:
        print("Greška: Morate unijeti cijeli broj!")

def indeks_u_listi():
    try:
        lista = [1, 2, 3]
        indeks = int(input("Unesite indeks: "))
        print(lista[indeks])
    except IndexError:
        print("Greška: Indeks je van opsega!")
    except ValueError:
        print("Greška: Morate unijeti cijeli broj!")

def provjeri_godine(godine):
    if godine < 18:
        raise ValueError("Morate imati najmanje 18 godina!")
    return "Pristup odobren."

def unos_godina():
    try:
        godine = int(input("Unesite svoje godine: "))
        print(provjeri_godine(godine))
    except ValueError as e:
        print(f"Greška: {e}")
        
if __name__ == "__main__":
    while True:
        print("\nIzaberite opciju:")
        print("1 - Dijeljenje")
        print("2 - Čitanje fajla")
        print("3 - Unos broja")
        print("4 - Indeks u listi")
        print("5 - Unos godina")
        print("0 - Izlaz")
        izbor = input("Unesite broj opcije: ")
        if izbor == "1":
            dijeljenje()
        elif izbor == "2":
            citanje_fajla()
        elif izbor == "3":
            unos_broja()
        elif izbor == "4":
            indeks_u_listi()
        elif izbor == "5":
            unos_godina()
        elif izbor == "0":
            print("Izlaz iz programa.")
            break
        else:
            print("Neispravan unos, pokušajte ponovo.")
