from flask.views import MethodView
from wtforms import Form, IntegerField, StringField, SubmitField
from flask import Flask, render_template, request

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
        amount = bill_form.amount.data
        return amount

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
