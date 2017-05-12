from flask import Blueprint, render_template

mod = Blueprint('welcome', __name__)


@mod.route('/')
@mod.route("/index")
def index():
    return render_template('index.html')
