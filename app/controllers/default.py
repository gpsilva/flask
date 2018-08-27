from app import app

@app.route("/index")
@app.route("/")
def index():
    return "Hello World!"

@app.route("/test", defautls={'name': None})
@app.route("/test/<name")
def test(name):
    if name:
        return "Hello, $s!" % name
    else:
        return "Hello, user!"
