from api_data.extensions import db
import pandas as pd
from io import BytesIO
from openpyxl import Workbook

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
