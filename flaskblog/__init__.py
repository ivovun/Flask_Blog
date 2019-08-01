from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskblog.forms import RegistrationForm, LoginForm

app = Flask(__name__)
app.config['SECRET_KEY'] = '8386f94a82224b6acdacaa022658018c'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routs
