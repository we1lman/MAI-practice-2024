import json


class DecisionEngine:
    def __init__(self):
        self.questions = self.load_data('data/questions.json')
        self.outcomes = self.load_data('data/outcomes.json')

    def load_data(self, filepath):
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)

    def get_recommendations(self, answers, scores):
        scores_map = {
            'math_modeling': 0,
            'statistical_analysis': 0,
            'software_systems': 0,
            'informatics': 0
        }

        for idx, answer in enumerate(answers):
            question = self.questions[idx]
            for option in question['options']:
                if answer == option['answer']:
                    for key in option['influence']:
                        scores_map[key] += option['influence'][key]

        recommendations = sorted(self.outcomes.values(), key=lambda x: scores_map.get(x['key'], 0), reverse=True)
        form_of_study = self.determine_form_of_study(scores)
        for rec in recommendations:
            rec['form_of_study'] = form_of_study
        return recommendations[:2]  # Возвращаем 1-2 лучших результата

    def determine_form_of_study(self, scores):
        total_score = scores['math'] + scores['informatics'] + scores['russian']
        if total_score >= 250:
            return ["бюджетное"]
        elif 220 <= total_score < 250:
            return ["целевое", "платное"]
        elif 210 <= total_score < 220:
            return ["платное"]
        else:
            return ["нет доступных форм обучения"]
