"""
John Doe's Flask API.
"""

import configparser    # Configure from .ini files and command line
from os import path
from flask import Flask, abort, send_from_directory, render_template

app = Flask(__name__)

@app.route("/")
def hello():
    if '~' in str(request.path):
        abort(403)
    if '/..' in str(request.path):
        abort(403)
    if path.exists(str(request.path)):
        render_template(request.path), 200
    else:
        abort(404)


@app.errorhandler(403)
def forbidden(e):
    return send_from_directory('./pages', '403.html'), 403


@app.errorhandler(404)
def forbidden(e):
    return send_from_directory('./pages','404.html'), 404


@app.errorhandler(401)
def forbidden(e):
    return send_from_directory('./pages','401.html'), 401


if __name__ == "__main__":
    config = configparser.ConfigParser()
    if path.exists('./credentials.ini'):
        config.read("credentials.ini")
    else:
        config.read("default.ini")
    SERVER = config['SERVER']
    app.run(debug=config.get('SERVER', 'DEBUG'), host='0.0.0.0', port=config.get('SERVER', 'PORT'))
