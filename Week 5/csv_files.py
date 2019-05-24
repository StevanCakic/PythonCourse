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


with open("google_stock_data.csv", newline="") as file: # newline zbog /n kod nekih OS
    reader = csv.reader(file)
    header = next(reader) # Ucitaj prvi red
    print(header)
    print("datetime", "float", "  float", "  float", "  float", "  integer", "   float")
    
    # Dio jedan
    '''
    data = [row for row in reader] # Ucitaj ostatak podataka
    print(data[0])
    
    '''

    # Dio dva, zakomentarisati dio 1
    '''
    from datetime import datetime
    result = []

    for row in reader:
        date = datetime.strptime(row[0], "%m/%d/%Y")
        open_price = float(row[1])
        high = float(row[2])
        low = float(row[3])
        close = float(row[4])
        volume = int(row[5])
        adj_close = float(row[6])
        result.append([date, open_price, high, low, close, volume, adj_close])

    print(result[0])
    '''

    # Zadatak da izracunamo stock daily return, 
    # tj. procentualnu razliku za dva susjedna dana (adj close)
    # U novom fajlu trebamo da imamo dvije kolone i to: Date i stock daily return (in perc)
    # Cesto se trazi da se ovo racuna osim po danima, i po nedeljama, mjesecima, godinama
    # Vremeno cemo nauciti kako se to radi

    '''
    with open("google_returns.csv", "w", newline="") as return_file: # probajte da upisete 
                                                                     # u fajl bez newline=""
        writer = csv.writer(return_file)
        writer.writerow(["Date", "Return"])
        # Srecom, podaci su vec sortirani po danima
        # Tako da mozemo lako da uporedimo vrijednost akcija za susjedne dane
        result_len = len(result)
        for index, row in enumerate(result):
            if index == result_len - 1:
                break
            todays_row = row
            todays_date = todays_row[0]
            todays_price = todays_row[-1]
            yesterday_row = result[index + 1]
            yesterday_date = yesterday_row[0]
            yesterday_price = yesterday_row[-1]

            daily_return = 100 * ((todays_price - yesterday_price) / yesterday_price)
            formated_date = todays_date.strftime("%m/%d/%Y")
            writer.writerow([formated_date, round(daily_return,3)])
    '''