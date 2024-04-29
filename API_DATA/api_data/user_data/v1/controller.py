from api_data.extensions import db
import pandas as pd
from io import BytesIO
from openpyxl import Workbook
from sqlalchemy import text

from flask import make_response, jsonify, send_file, Response


def calculate_interest(req):
    principal = float(req["principal"])
    rate = float(req["rate"])
    time = float(req["time"])
    interest = (principal * rate * time) / 100
    response = {
        "interest": interest
    }
    return make_response(jsonify(response), 200)

def export_excel(transcribed_texts):
    df=pd.DataFrame(transcribed_texts)
    excel_file_path = 'output.xlsx'
    df.to_excel(excel_file_path, index=False)


def searchData(req):
    select_dropdown=req["dropdown"]
    search_input=req["search"]
    user_dropdown=select_dropdown
    if select_dropdown.lower()=="city":
        user_dropdown="country"
    customer_data=db.session.execute(text(f"""select name, age, city from customer_data where {select_dropdown} like '%{search_input}%'"""))
    customer_df=pd.DataFrame(customer_data)
    customer_dict=customer_df.to_dict("records")
    user_data=db.session.execute(text(f"""select name, age, country as city from user_data where {user_dropdown} like '%{search_input}%'"""))
    user_df=pd.DataFrame(user_data)
    user_dict=user_df.to_dict("records")
    staff_data=db.session.execute(text(f"""select name, age, city from staff_data where {select_dropdown} like '%{search_input}%'"""))
    staff_df=pd.DataFrame(staff_data)

    staff_dict=staff_df.to_dict("records")

    response={"User Data": user_dict, "Staff Data": staff_dict, "Customer Data": customer_dict}
    return make_response(jsonify(response), 200)