from flask import Flask

print(__name__)

app = Flask(__name__)

# route dekorator, cesto cemo ga koristiti
@app.route("/") # adresa server /, npr. https://google.com/
def home():
    return "Hello"

app.run(port=5000)