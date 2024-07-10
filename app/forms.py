from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email, NumberRange

class UserForm(FlaskForm):
    name = StringField('ФИО', validators=[
        DataRequired(message="Введите ФИО полностью.")
    ])
    email = StringField('Электронная почта', validators=[
        DataRequired(message="Введите корректный email."),
        Email()
    ])
    interests = StringField('Интересы', validators=[
        DataRequired(message="Введите ваши интересы.")
    ])
    math_score = IntegerField('Баллы по математике', validators=[
        DataRequired(),
        NumberRange(min=0, max=100, message="Пожалуйста, выберите значение от 0 до 100.")
    ])
    informatics_score = IntegerField('Баллы по информатике', validators=[
        DataRequired(),
        NumberRange(min=0, max=100, message="Пожалуйста, выберите значение от 0 до 100.")
    ])
    russian_score = IntegerField('Баллы по русскому языку', validators=[
        DataRequired(),
        NumberRange(min=0, max=100, message="Пожалуйста, выберите значение от 0 до 100.")
    ])
    submit = SubmitField('Получить рекомендации')
