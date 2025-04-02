from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, RadioField, IntegerField, validators

class StrikeForm(FlaskForm):
    name = StringField("Wat is je naam?", validators=[validators.DataRequired()])
    strike = RadioField("Ga je staken?", choices=[("y", "Ja"), ("n", "Nee")])
    age = IntegerField("Wat is je leeftijd?", validators=[validators.NumberRange(18)])
    submit = SubmitField("Verzend")