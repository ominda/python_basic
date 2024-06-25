from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

@app.route("/python")
def python():
    return "<h1>Hello, Python</h1>"