import csv


# print(dir(csv))

# Prije nego krenemo sa citanjem iz fajla, pogledajmo kako radi funkcija next()
'''
random = [5, 9, 'cat']

# converting list to iterator
randomIterator = iter(random)
print(randomIterator)

# Output: 5
print(next(randomIterator))

# Output: 9
print(next(randomIterator))

# Output: 'cat'
print(next(randomIterator))

# This will raise Error
# iterator is exhausted
print(next(randomIterator))

'''


with open("../assets/google_stock_data.csv", newline="") as file: # newline zbog /n kod nekih OS
    reader = csv.reader(file)
    header = next(reader) # Ucitaj prvi red
    print(header)
    print("datetime", "float", "  float", "  float", "  float", "  integer", "   float")
    
    # Dio jedan
    '''
    data = [row for row in reader] # Ucitaj ostatak podataka
    print(data[0])
    
    '''