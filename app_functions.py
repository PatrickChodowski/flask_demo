
from flask_wtf import FlaskForm
from wtforms import SelectField, IntegerField, FloatField
from wtforms.validators import DataRequired, NumberRange

class ModelForm(FlaskForm):


    ilosc = IntegerField('Ilosc', [NumberRange(min=0, max=5)])
    bike = SelectField('Rower', choices=['orbea', 'specialized', 'pinarello', 'trek', 'kross', 'btwin'],
                       validators=[DataRequired()])
    #cena = FloatField('Cena roweru', [NumberRange(min=0, max=10000)])
