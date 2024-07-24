import os

class Config:
    SECRET_KEY = 'hard_to_guess_string'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
