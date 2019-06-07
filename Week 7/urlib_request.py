from urllib import request
import time

# print(dir(request))

resp = request.urlopen("https://en.wikipedia.org/wiki/Main_Page")

print(type(resp)) # pazite, ovo nije reponse iz urllib modula

print(dir(resp))

print(resp.code)
print(resp.length) # velicina odgovora u bajtima
print(resp.peek()) # read chunk of data

data = resp.read() # read data
print(data)
print(type(data))
print("*********************")
time.sleep(2)

# Kako da pretvorim byte reprezentaciju u string?
html = data.decode("UTF-8")
print(html)
print(type(html))

# Sta ako opet pokusamo da procitamo response?
print(resp.read()) # zasto?