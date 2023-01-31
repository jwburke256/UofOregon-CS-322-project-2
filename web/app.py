"""
John Doe's Flask API.
"""

import configparser    # Configure from .ini files and command line
from os import path
from flask import Flask, abort, send_from_directory, render_template

app = Flask(__name__)

@app.route("/<path:request>")
def hello(request):
    if '~' in str(request):
        abort(403)
    if '..' in str(request):
        abort(403)
    return send_from_directory('./pages', request), 200

@app.errorhandler(403)
def forbidden(e):
    return send_from_directory('./pages', '403.html'), 403


@app.errorhandler(404)
def notfound(e):
    return send_from_directory('./pages','404.html'), 404


if __name__ == "__main__":
    config = configparser.ConfigParser()
    if path.exists('./credentials.ini'):
        config.read("credentials.ini")
    else:
        config.read("default.ini")
    SERVER = config['SERVER']
    app.run(debug=config.get('SERVER', 'DEBUG'), host='0.0.0.0', port=config.get('SERVER', 'PORT'))
