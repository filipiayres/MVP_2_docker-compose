import os

class Config:
    BASE_DIR = os.path.abspath(os.path.dirname(__file__))
    
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{BASE_DIR}/hospital.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = False
    
    SWAGGER_URL = '/api/docs'
    API_URL = '/swagger.json'