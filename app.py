from flask import Flask, render_template
import utils

app = Flask(__name__)

file_adress = "https://jsonkeeper.com/b/89KW"

candidates = utils.load_candidates_from_json(file_adress)


@app.route('/')
def get_list_all():
    return render_template('list.html', candidates=candidates)


if __name__ == '__main__':
    app.run()
