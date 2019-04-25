# While loop primjeri

'''
i = 1
while i < 6:
  print(i)
  i += 1
'''

# Primjer sa break
'''
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
'''
# Primjer za continue
'''
i = 0
while i < 6:
  i += 1 
  if i == 3:
    continue
  print(i)
'''

# While petlje kod Pythona imaju else dio
'''
i = 0
while i < 6:
    i += 1 
else:
    print("Done")
'''

# For loop primjer

# Iteracija kroz listu
'''
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    print(x)
'''

# Iteracija kroz torku
'''
fruits = ("apple", "banana", "cherry")
for x in fruits:
    print(x)
'''

# Iteracija kroz string
'''
for x in "banana":
  print(x)
'''

# Kombinacije liste sa torkama
'''
l = [(1, 2), (3, 4), (5, 6)]
for (t1, t2) in l:
    print(t1)
'''

# Primjer sa range
for elem in range(0, 10):
    print(elem)

for elem in range(0, 10, 2):
    print(elem)


# list(range(100))

