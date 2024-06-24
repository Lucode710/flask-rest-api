from flask import Flask
from src.api import Api
from src.config import *

# create and configure the app
def create_app():
    app = Flask(__name__)

     # set development configuration 
    app.config.from_object(DevelopmentConfig())

    return app

app = create_app()

api = Api(app)