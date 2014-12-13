import os

dirpath = os.path.abspath(os.path.dirname(__file__))

TESTING = True
DEBUG = False
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + dirpath + '/' + 'test.db'
