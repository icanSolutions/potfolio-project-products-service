import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite:///products.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ENV = os.getenv('FLASK_ENV', 'production')
    DEBUG = os.getenv('DEBUG', 'false').lower() == 'true'
    TESTING = False
