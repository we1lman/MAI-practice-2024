from flask import Blueprint, render_template, request
from .forms import UserForm
from .utils.decision_engine import DecisionEngine
import json
import os

bp = Blueprint('main', __name__)


@bp.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm()
    if form.validate_on_submit():
        user_data = {
            'name': form.name.data,
            'email': form.email.data,
            'interests': form.interests.data,
            'scores': {
                'math': form.math_score.data,
                'informatics': form.informatics_score.data,
                'russian': form.russian_score.data
            }
        }

        save_user_data(user_data)

        decision_engine = DecisionEngine()
        questions = decision_engine.questions
        return render_template('questions.html', form=form, questions=questions, interests=user_data['interests'],
                               scores=user_data['scores'])
    return render_template('index.html', form=form)


@bp.route('/results', methods=['POST'])
def results():
    interests = request.form.get('interests')
    scores = {
        'math': int(request.form.get('math')),
        'informatics': int(request.form.get('informatics')),
        'russian': int(request.form.get('russian'))
    }
    answers = []
    for i in range(1, 6):
        answers.append(request.form.get(f'question_{i}'))

    decision_engine = DecisionEngine()
    recommendations = decision_engine.get_recommendations(answers, scores)
    return render_template('results.html', recommendations=recommendations)


def save_user_data(user_data):
    data_path = os.path.join('app', 'data/user_data.json')
    if not os.path.exists(data_path):
        with open(data_path, 'w', encoding='utf-8') as file:
            json.dump([], file)

    with open(data_path, 'r+', encoding='utf-8') as file:
        data = json.load(file)
        data.append(user_data)
        file.seek(0)
        json.dump(data, file, ensure_ascii=False, indent=4)
