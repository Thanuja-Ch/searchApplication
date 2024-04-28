from os import getenv
from flask import Flask,jsonify,request
import pymssql
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from api_data import extensions
from flask import Blueprint
from flask_restx import Api as RestX_Api
from api_data.extensions import db

from api_data.commands import userdata

import click
from flask.cli import with_appcontext

from .user_data.v1 import open_api

api_blueprint = Blueprint("api", __name__, url_prefix="/api")


# initialize restx
rest_api = RestX_Api(
    api_blueprint,
    title="api_data"
)

rest_api.add_namespace(open_api,path='/v1')


def create_app():
    app = Flask(__name__)

    app.config.from_object(get_config_object_path())

    app.register_blueprint(api_blueprint)


     # initializing all extensions
    extensions.init_extensions(app)
    
    @app.route('/')
    def home():
        return "<h2>Hello world!! Welcome to Home Page <h2>"


    app.cli.add_command(userdata)
         
    return app


def get_config_object_path():
    dev_config = "api_data.config.DevelopmentConfig"
    env = getenv('FLASK_ENV')
    environment_config = dev_config
    if env == 'developement':
        environment_config = dev_config
    
    return environment_config

