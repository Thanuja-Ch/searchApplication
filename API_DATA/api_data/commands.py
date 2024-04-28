import pandas as pd
import click
from flask.cli import with_appcontext
from api_data.user_data.models import UserData, StaffData, CustomerData
from .extensions import db
import os

customer_mapping = {
  "Customer ID": "customer_id",
  "Name": "name",
  "Age": "age",
  "City": "city",
  "Last Purchase Amount (USD)": "last_purchase_amount"
}
staff_mapping = {
    'Name': "name",
    'Age': "age",
    'Gender': "gender",
    'Occupation': "occupation", 
    'City': "city",
    'Email': "email",
    'Phone': "mobile",
}
user_mapping = {
    'Name': "name",
    'Age': "age",
    'Country': "country",
    'Mobile': "mobile", 
    'Email': "email"
}

current_dir = os.path.dirname(os.path.realpath(__file__))
def pipe_df(file_name):
    data=[]
    file_path = os.path.join(current_dir, f"../../assets/{file_name}")

    with open(file_path, 'r') as file:
        for line in file:
            fields = line.strip().split('|')
            data.append(fields)
    df = pd.DataFrame(data[1:], columns=data[0])
    df.columns = df.columns.str.strip()
    df = df.apply(lambda x: x.str.strip() if x.dtype == "object" else x)
    return df


@click.command(name="userdata")
@with_appcontext
def userdata():
    UserData.query.delete()
    db.session.commit()
    list_df=pipe_df("NxtWave_Raw")
    list_df.rename(
            columns = user_mapping,
            inplace = True,
        )
    list_df=list_df.to_dict("records")
    db.session.execute(UserData.__table__.insert(),list_df)
    db.session.commit()
    print("Data inserted successfully")


@click.command(name="staffdata")
@with_appcontext
def staffdata():
    StaffData.query.delete()
    db.session.commit()
    list_df=pipe_df("Raw_data_1")
    list_df.rename(
            columns = staff_mapping,
            inplace = True,
        )
    list_df=list_df.to_dict("records")
    db.session.execute(StaffData.__table__.insert(),list_df)
    db.session.commit()
    print("Data inserted successfully")

@click.command(name="customerdata")
@with_appcontext
def customerdata():
    CustomerData.query.delete()
    db.session.commit()
    file_path = os.path.join(current_dir, "../../assets/Raw_Data")
    df = pd.read_csv(file_path, sep="\t")
    df['Last Purchase Amount (USD)'] = df['Last Purchase Amount (USD)'].str.replace('$', '').astype(float)
    df = df.dropna(axis=1)
    df.rename(
            columns = customer_mapping,
            inplace = True,
        )
    list_df=df.to_dict("records")
    db.session.execute(CustomerData.__table__.insert(),list_df)
    db.session.commit()
    print("Data inserted successfully")