import os

from flask import Flask

app = Flask(__name__)
# app.config.from_pyfile('settings.cfg')
app.secret_key = os.urandom(128)

from idlerpg_site_flask.web.views import index, playerinfo

app.register_blueprint(index.mod)
app.register_blueprint(playerinfo.mod)
