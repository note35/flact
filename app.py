import os

from flask import Flask  # type: ignore

from view.base import base_blueprint


application_root = os.path.abspath('.')
static_folder = os.path.join(application_root, 'static')
template_folder = os.path.join(application_root, 'templates')

app = Flask(__name__, static_url_path='/static', static_folder=static_folder, template_folder=template_folder)
app.register_blueprint(base_blueprint)
