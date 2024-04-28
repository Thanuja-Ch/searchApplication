import pandas as pd
import click
from flask.cli import with_appcontext
from api_data.user_data.models import UserData, StaffData, CustomerData
from .extensions import db

@click.command(name="userdata")
@with_appcontext
def userdata():
    df=pd.read_excel("path/",sheet_name='',skiprows=1)
    list_df_user=df.to_dict("records")
    db.engine.execute(UserData.__table__.insert(),list_df_user)
    print("Data inserted successfully")



