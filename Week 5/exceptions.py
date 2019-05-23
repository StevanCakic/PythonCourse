# print(2 + "3")

# Type error
'''
try:
    print(2 + "3")
except :
    print("Something went wrong")
else: # izvrsi se ako se try uspjesno izvrsi
    print("Else")
finally: # izvrsi se bez obzira na sve
    print("Finally")
'''

# IOError
'''
try:
    f = open("file.txt", "w") # obrisati fajl i probati sta ce se desiti ako probamo
                              # da procitamo fajl koji ne postoji
    f.write("Tekst")
except:
    print("Cant write to file")
else:
    print("Write to file was successful")
'''

# Check this :)

'''
def get_val_basic():
    try:
        input_user = int(input("Please enter an integer:"))
    except:
        print("Looks like you did not enter integer")
        input_user = int(input("Try again - please enter an integer"))
    finally:
        print("This block executed")
    print(input_user)

get_val_basic()

def get_val():
    while True:
        try:
            input_user = int(input("Please enter an integer:"))
        except:
            print("Looks like you did not enter integer")
            continue
        else:
            print("Correct. Integer.")
            break
        finally:
            print("This block executed")
        print(input_user)

get_val()
'''

# Working with math

import math

print(math.sqrt(-1))

# Kako ovo da rijesimo
# Kako da "bacite izuzetak"

