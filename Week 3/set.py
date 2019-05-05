# Skupovi

'''
skup1 = set()
skup2 = set()

skup1.add(1)
skup1.add(2)
skup2.add(1)
skup2.add(2)
skup2.add(3)

# Kako da napravimo ovo u dvije linije koda, da ne dodajemo jedan po jedan element?

print(skup1.intersection(skup2))
print(skup1.union(skup2))
print(skup1.issubset(skup2))
print(skup2.issuperset(skup1))
print(skup2.difference(skup1))
print(skup2.isdisjoint(skup1)) # ako nemaju zajednickih elementata true, inace false

# Postoje i metode difference_update, intersection_update koji mijenjaju skup
# nad kojim se poziva metod u rezultat ovih metoda

skup2.add(1)
print(skup2)
skup2.discard(2)
skup2.remove(1)
# Razlika izmedju discard i remove je ta sto ako pokusate da uklonite element koji ne postoji
# discard ne vraca gresku, dok remove vraca
print(skup2)

lista = [1,1,1,2,2,3]
print(set(lista))

'''