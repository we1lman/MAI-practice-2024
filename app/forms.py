from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, NumberRange

class UserForm(FlaskForm):
    interests = StringField('Интересы', validators=[DataRequired()])
    math_score = IntegerField('Баллы по математике', validators=[DataRequired(), NumberRange(min=0, max=100)])
    informatics_score = IntegerField('Баллы по информатике', validators=[DataRequired(), NumberRange(min=0, max=100)])
    russian_score = IntegerField('Баллы по русскому языку', validators=[DataRequired(), NumberRange(min=0, max=100)])
    submit = SubmitField('Получить рекомендации')
