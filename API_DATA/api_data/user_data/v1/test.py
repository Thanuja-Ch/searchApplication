from io import BytesIO
from openpyxl import Workbook
from flask import send_file, Flask

def export_excel(transcribed_texts):
    transcribed_texts = transcribed_texts["transcribed_texts"]
    wb = Workbook()
    ws = wb.active
    ws.title = 'transcribed_texts'
    column_names = ['Transcribed Texts']
    ws.append(column_names)

    for row in transcribed_texts:
        ws.append([row])

    excel_data = BytesIO()
    wb.save(excel_data)
    excel_data.seek(0)

    return send_file(
        excel_data,
        mimetype="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        as_attachment=True,
        download_name="transcribed_texts.xlsx"
    )

app = Flask(__name__)

@app.route('/download_excel')
def download_excel():
    # This is an example route where the export_excel function is called
    transcribed_texts = {"transcribed_texts": ["a", "b", "c"]}
    return export_excel(transcribed_texts)


if __name__ == '__main__':
    app.run(debug=True)
