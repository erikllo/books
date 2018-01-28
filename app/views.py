from app import app
from flask import render_template

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello Toffee!</h1>"
@app.route("/maple")
def maple():
    return "<h1 style='color:brown'>Hello Maple!</h1>"
@app.route("/example")
def example():
    return render_template('example.html')
