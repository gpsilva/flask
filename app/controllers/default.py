from flask import render_template
from app import app

@app.route("/index")
@app.route("/")
def index():
    return render_template('index.html')

# @app.route("/test", defautls={'name': None})
#@app.route("/test/<name")
#def test(name):
#   if name:
#        return "Hello, $s!" % name
#    else:
#        return "Hello, user!"
