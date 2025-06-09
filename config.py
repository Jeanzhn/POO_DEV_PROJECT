import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///banco_de_dados.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.urandom(24)
    