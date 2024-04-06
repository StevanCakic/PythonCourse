from urllib import request
import json

content = request.urlopen("https://jsonblob.com/api/1226135479824277504").read()
print(json.loads(content.decode()))

