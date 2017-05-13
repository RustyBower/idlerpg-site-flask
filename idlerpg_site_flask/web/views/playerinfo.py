from flask import Blueprint, render_template

mod = Blueprint('playerinfo', __name__)


@mod.route('/playerinfo')
def playerinfo():
    return render_template('playerinfo.html')
