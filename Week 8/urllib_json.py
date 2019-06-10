from urllib import request
import json

content = request.urlopen("https://api.myjson.com/bins/1h8a4d").read()
print(json.loads(content.decode())["data"])

