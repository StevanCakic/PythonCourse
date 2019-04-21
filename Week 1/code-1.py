# Prvi dio
# Varijable

# Zadatak 1
# Kreirati sledeće varijable:
    # ime koja sadrži vaše ime
    # prezime koja sadrži vaše prezime
    # godine koja sadrži vaše godine
    # email koja sadrži vašu email adresu
# Štampati rezultat u sledećem formatu:
    # Email adresa korisnika {ime} {prezime} ({godine}) je {email}.

ime = "Stevan"
prezime = "Čakić"
godine = 25
email = "stevancakic93@gmail.com"

print("Email adresa korisnika " + ime + " " + prezime + " (" + str(godine) + ") je " + email + "." )
# print(f"Email adresa korisnika {ime} {prezime} ({godine}) je {email}.")


# Drugi dio
# Brojevi

# Isprobajte aritmetičke operacije sa integer i floating brojevima. 
    # Sta je rezultat operacije 0.1 + 0.2?
    # Isporbati operator **
        # Kako da nađete korijen broja koristeći ** operator?
    # Isprobati operator eksponent (e)
        # Šta je rezultat 4e2
# Zadatak 2
# Ako je cijena računara 400e, štampati koliko treba odvojite za plaćanje PDVa
# Štampati rezultat u sledećem formatu:
    # Cijena računara je 400e. Iznos PDVa je {pdv}, a cijena računara bez PDVa je {cijena bez PDVa}

cijena_racunara = 400

pdv = 0.21 * 400

print(f"Cijena racunara je {cijena_racunara}. Iznos PDVa je {pdv}, a cijena racunara bez PDVa je {cijena_racunara - pdv}")



# Treci dio
# Casting

# Isprobati par konverzija iz jednog tipa podatka u drugi
