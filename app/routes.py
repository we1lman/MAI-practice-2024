from flask import Blueprint, render_template, request, redirect, url_for
from .forms import UserForm
from .utils.decision_engine import DecisionEngine

bp = Blueprint('main', __name__)

@bp.route('/', methods=['GET', 'POST'])
def index():
    form = UserForm()
    if form.validate_on_submit():
        interests = form.interests.data
        scores = {
            'math': form.math_score.data,
            'informatics': form.informatics_score.data,
            'russian': form.russian_score.data
        }
        decision_engine = DecisionEngine()
        questions = decision_engine.questions
        return render_template('questions.html', form=form, questions=questions, interests=interests, scores=scores)
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
