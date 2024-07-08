import os

FLASK_SECRET_APP = 'Z}WB[03kLz{YB?5*\x0cFGhb*YT'
FLASK_DEBUG = True
basedir = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(basedir, "app.db")
SQLALCHEMY_ECHO = True
JWT_SECRET_KEY = '404e7e6cf343fc4163722427'

print(SQLALCHEMY_DATABASE_URI)

