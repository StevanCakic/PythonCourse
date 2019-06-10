from urllib import parse

# https://www.youtube.com/watch?v=mpnBNGOSplA&t=10

print(dir(parse))

params = {"v": "mpnBNGOSplA", "t": "1m56s"}

querystring = parse.urlencode(params)
print(querystring)
url = f"https://www.youtube.com/watch?{querystring}"
print(url)
