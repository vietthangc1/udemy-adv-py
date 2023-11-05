from flask.views import MethodView
from wtforms import Form, IntegerField, StringField, SubmitField
from flask import Flask, render_template, request

from flatmates_bill.pkg.flat.bill import Bill
from flatmates_bill.pkg.flat.flatmate import Flatmate
from flatmates_bill.pkg.exporter.pdf import PDFExporter, FileStackUpload

app = Flask(__name__)

class HomePage(MethodView):
    def get(self):
        return render_template('index.html')

class BillFormPage(MethodView):
    def get(self):
        bill_form = BillForm()
        return render_template('bill_form.html', bill_form = bill_form)

class ResultsPage(MethodView):
    def post(self):
        bill_form = BillForm(request.form)
        period = bill_form.period.data
        amount = int(bill_form.amount.data)

        name1 = bill_form.name1.data
        days1 = int(bill_form.days1.data)
        name2 = bill_form.name2.data
        days2 = int(bill_form.days2.data)

        flatmate1 = Flatmate(name1, days1)
        flatmate2 = Flatmate(name2, days2)
        flatmates = [flatmate1, flatmate2]
        bill = Bill(amount=amount, flatmates= flatmates, period= period)

        pdf = PDFExporter(bill)
        pdf.export(border=False)

        file = FileStackUpload()
        url = file.upload()

        return render_template("result.html", url_file = url)
        
class BillForm(Form):
    amount = StringField('Bill Amount: ')
    period = StringField('Period: ')

    name1 = StringField('Name: ')
    days1 = IntegerField('Days: ')

    name2 = StringField('Name: ')
    days2 = IntegerField('Days: ')

    button = SubmitField('Calculate')

app.add_url_rule('/', view_func=HomePage.as_view('home_page'))
app.add_url_rule('/bill', view_func=BillFormPage.as_view('bill_form_page'))
app.add_url_rule('/result', view_func=ResultsPage.as_view('result_page'))

if __name__ == '__main__':
    app.run(port=3030)