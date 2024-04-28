from api_data.extensions import db
from flask import make_response, jsonify


def calculate_interest(req):
    principal = req["principal"]
    rate = req["rate"]
    time = req["time"]
    interest = (principal * rate * time) / 100
    response = {
        "interest": interest
    }
    return make_response(jsonify(response), 200)