from api_data.extensions import db,ma
from flask_marshmallow import fields

from sqlalchemy import (
    Column,
    DECIMAL,
    ForeignKey,
    Index,
    Integer,
    String,
    Text,
    NVARCHAR,
    BigInteger
)
class UserData(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(200))
    age=db.Column(db.Integer)
    country=db.Column(db.String(200))
    mobile=db.Column(db.String(200))
    email=db.Column(db.String(250))

class CustomerData(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    customer_id=db.Column(db.String(50))
    name=db.Column(db.String(50))
    age=db.Column(db.Integer)
    city=db.Column(db.String(50))
    last_purchase_amount=db.Column(db.Integer)
    

class StaffData(db.Model):
    id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(200))
    age=db.Column(db.Integer)
    gender=db.Column(db.String(200))
    occupation=db.Column(db.String(200))
    city=db.Column(db.String(200))
    email=db.Column(db.String(250))
    mobile=db.Column(db.String(200))