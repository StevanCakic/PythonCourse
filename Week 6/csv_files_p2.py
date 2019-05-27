import csv

with open('names.csv',"w", newline='') as csvfile:
    fieldnames = ["first_name", "last_name"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name':"Marko", "last_name":"Markovic"})
    writer.writerow({'first_name':"Petar", "last_name":"Petrovic"})
    writer.writerow({'first_name':"Nikola", "last_name":"Nikolic"})

with open('names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        print(row['first_name'], row['last_name'])

