from app import app

@app.route("/")
def hello():
    return "<h1 style='color:blue'>Hello Toffee!</h1>"
@app.route("/maple")
def maple():
    return "<h1 style='color:brown'>Hello Maple!</h1>"
