from flask import Blueprint, render_template

games = Blueprint('games', __name__, template_folder='templates')

@games.route('/')
def index():
    return render_template('pages/index.html',page='games page')