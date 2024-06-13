from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__, static_folder='static')
app.config['SECRET_KEY'] = '40a05c4174512cbd95b6e28cf037fe73'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config["SQLALCHEMY_DATABASE_URI"] = 'postgresql://anonyme:anonyme@localhost:5432/flask_project'
# format alternatif (copié) :
# #app.config["SQLALCHEMY_DATABASE_URI"] ='jdbc:postgresql://localhost:5432/flask_project'
db = SQLAlchemy(app)
from . import routes
