from flask import Blueprint, render_template

mod = Blueprint('index', __name__)


@mod.route('/')
@mod.route('/index')
def index():
    return render_template('index.html')
