from . import controller as c
from api_data.extensions import db

from flask_restx import Namespace,Resource
from flask import jsonify,request
import pandas as pd

open_api=Namespace("openapi")

@open_api.route('/interest-calculator')
class InterestCalculator(Resource):
    def post(self):
        req = request.get_json()
        return c.calculate_interest(req)