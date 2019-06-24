# Potrebno je koristiti modul pymongo

# Konektujte se na mongod server

# Kreirati bazu cije je ime vjezbanje

# U njoj kreirati kolekciju students

# Svaki student opisan je sledecim atributima

  # ime - String od 3 do 10 karaktera
  # prezime - String od 3 do 10 karaktera
  # godina_rodjena - Int duzine 4 (samo godina rodjenja)
  # broj_indeksa - String duzinje 5 (01/19 ili 11/19 itd. maks 99/19)
  # godina_studiranja - Int od 1 do 8 
  # prosjek - Double, ne manji od 5 i ne veci od 10

# Kreirati adekvatnu shemu za validaciju

# Nakon toga dodati bar 10 studenata (testirati da li kada se unesu pogresni podaci vasa
# sema za validaciju blokira dodavanje studenta u bazu)  

# Napisati sledece upite (find)

# Izdvojiti sve studente prve godine
# Izdvojiti sve studente ciji se broj indeksa zavrsava sa /18
# Izdvojiti sve studente ciji je prosjek veci od 8 i cija je godina studija 3 
#   (izdvojiti samo ime, prezime i prosjek tih studenta)
# Izdvojiti sve studente rodjenje nakon 1998 godine koji su na prvoj godini studija
# Izdvojiti sve studente sa prve i druge godine studija   
# Izdvojiti 3 najmladja studenta sortirana po prezimenu u opadajucem poretku 

# Brisanje studenata (delete)
# Ukloniti sve studente sa zadnje godine studija

# Azuriranje studenata (update)
# Azurirate godinu studija svim studentima koji nisu na zadnjoj (8-oj godini studija)