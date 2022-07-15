from flask import Flask, render_template
import utils

app = Flask(__name__)

file_adress = "https://jsonkeeper.com/b/89KW"

candidates = utils.load_candidates_from_json(file_adress)


@app.route('/')
def get_list_all():
    return render_template('list.html', candidates=candidates)


@app.route('/candidate/<int:id>')
def get_candidate_card(id):
    candidate = utils.get_candidate(candidates, id)
    return render_template('card.html', candidate=candidate)


@app.route('/candidate/<candidate_name>')
def get_candidate_name(candidate_name):
    candidate = utils.get_candidate_by_name(candidates, candidate_name)
    return render_template('search.html', candidate=candidate)


@app.route('/skill/<skill>')
def get_candidate_skill(skill):
    candidate = utils.get_candidate_by_skill(candidates, skill)
    return render_template('skill.html', candidate=candidate, skill=skill)


if __name__ == '__main__':
    app.run(debug=True)
