import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

basedir = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
print(basedir)
app = Flask(__name__, template_folder='../templates', static_folder='../static')
app.config.from_mapping(
    SECRET_KEY='super-secret',
    SQLALCHEMY_DATABASE_URI='sqlite:///' + os.path.join(basedir, 'databases.db'),
    SQLALCHEMY_TRACK_MODIFICATIONS=False
)

db = SQLAlchemy(app)

login = LoginManager(app)