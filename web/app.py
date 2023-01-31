"""
John Doe's Flask API.
"""

import configparser    # Configure from .ini files and command line
from os import path
from flask import Flask, abort, send_from_directory, render_template

app = Flask(__name__)

@app.route("/pages")
def hello():
    #print(path)
    #print(path.exists(request.path))
    if '~' in str(request.path):
        abort(403)
    if '/..' in str(request.path):
        abort(403)
    if path.exists(str(request.path)):
        render_template(request.path), 200
    #else:
        #abort(404)


    #return send_from_directory('pages/', 'trivia.html'), 200
    return render_template('<p>failure</p>'), 200

@app.errorhandler(403)
def forbidden(e):
    return send_from_directory('./pages', '403.html'), 403


@app.errorhandler(404)
def forbidden(e):
    return send_from_directory('./pages','404.html'), 404


@app.errorhandler(401)
def forbidden(e):
    return send_from_directory('./pages','401.html'), 401


#def get_options():
    """
    Options from command line or configuration file.
    Returns namespace object with option value for port
    """
    # Defaults from configuration files;
    #   on conflict, the last value read has precedence
    #options = config.configuration()
    # We want: PORT, DOCROOT, possibly LOGGING


if __name__ == "__main__":
    config = configparser.ConfigParser()
    if path.exists('./credentials.ini'):
        config.read("credentials.ini")
    else:
        config.read("default.ini")
    SERVER = config['SERVER']
    app.run(debug=config.get('SERVER', 'DEBUG'), host='0.0.0.0', port=config.get('SERVER', 'PORT'))
