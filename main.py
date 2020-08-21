from flask import Flask, render_template, request, redirect, url_for
import psycopg2 as pg
from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, FloatField, SubmitField
from wtforms.validators import DataRequired, NumberRange
import pandas as pd
import datetime as dt


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'
connection = pg.connect(user="postgres",
                              password="postgres",
                              host="127.0.0.1",
                              port="5432",
                              database="postgres")

cur = connection.cursor()
cur.execute('SELECT * FROM rowery;')
rower_data = cur.fetchall()
rower_df = pd.DataFrame(rower_data, columns=['id', 'nazwa', 'cena'])


class ModelForm(FlaskForm):
    ilosc = IntegerField('Ilosc', [NumberRange(min=0, max=5)])
    bike = SelectField('Rower', choices=rower_df['nazwa'].to_list(),
                       validators=[DataRequired()])
    submit = SubmitField('Kup')



@app.route('/')
def index():
    form = ModelForm()
    return render_template('index.html', form=form)

@app.route('/index_oblicz', methods=['POST'])
def index_oblicz():
    zakup = {'ilosc': int(request.form.getlist('ilosc')[0]),
             'nazwa': request.form.getlist('bike')[0]}
    zakup_df = pd.DataFrame(zakup, index=[0])

    zakup_df_cena = pd.merge(zakup_df, rower_df, on='nazwa', how='left')
    zakup_df_cena['koszyk'] = zakup_df_cena['cena'] * zakup_df_cena['ilosc']

    print(zakup_df_cena)
    query = """
            INSERT into transakcje(data, id_rower, wartosc, ilosc ) values('%s', %s, %s, %s);
            """ % (str(dt.date.today()),
                   zakup_df_cena['id'][0],
                   zakup_df_cena['koszyk'][0],
                   zakup_df_cena['ilosc'][0])

    cur.execute(query)
    connection.commit()
    return redirect(url_for("index"))


if __name__ == '__main__':
    app.run(debug=False, port=5003)


