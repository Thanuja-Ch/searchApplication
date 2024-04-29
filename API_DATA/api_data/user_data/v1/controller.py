from api_data.extensions import db
import pandas as pd
from io import BytesIO
from openpyxl import Workbook
from sqlalchemy import text

from flask import make_response, jsonify, send_file


def calculate_interest(req):
    principal = req["principal"]
    rate = req["rate"]
    time = req["time"]
    interest = (principal * rate * time) / 100
    response = {
        "interest": interest
    }
    return make_response(jsonify(response), 200)

def export_excel(transcribed_texts):
    wb = Workbook()
    ws = wb.active
    ws.title = 'transcribed_texts'
    column_names = ['Column1']
    ws.append(column_names)

    for row in transcribed_texts:
        ws.append(row)

    excel_data = BytesIO()
    wb.save(excel_data)
    excel_data.seek(0)
    return send_file(
        excel_data,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        as_attachment=True,
        download_name='transcribed_texts.xlsx'
    )

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