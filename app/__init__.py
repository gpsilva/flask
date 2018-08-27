from flask import Flask
from flask_sqlalchemy import flask_sqlalchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///storage.db'
db = SQLAlchemy(app)

from app.controllers import default

