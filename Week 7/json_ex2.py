import json

content = ""

with open("test.json", "r", encoding="utf-8") as json_file:
    content = json.load(json_file)
    print(type(content))
    print(content)
    print(content["data"][0]["lastName"])
    print(content["data"][1]["lastName"])

print(json.dumps(content))
print(json.dumps(content, ensure_ascii=False))


x =  '{"name":"Šon", "age":30, "city":"New York"}'
print(json.loads(x)["city"])

with open("new_test.json", "w", encoding="utf-8") as json_file:
    json.dump(x, json_file, ensure_ascii=False)


with open("new_test.json", "r", encoding="utf-8") as json_file:
    content = json.load(json_file)
    print(content)