from urllib import request
import json

content = request.urlopen("https://api.myjson.com/bins/76sg1").read()
print(json.loads(content.decode()))

