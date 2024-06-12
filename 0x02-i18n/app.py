#!/usr/bin/env python3
"""
Defines a flask app.
"""
from flask_babel import Babel
from flask import (
    Flask,
    g,
    render_template,
    request
    )


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Holds configuration values for the Flask app.
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.before_request
def before_request():
    """
    Sets the global user.
    """
    user = get_user()
    if user is not None:
        g.user = user


def get_user():
    """
    Returns the logged in user's dictionary.
    """
    user_id = request.args.get('login_as', None)
    if user_id is not None:
        user_id = int(user_id)
    return users.get(user_id, None)


@babel.localeselector
def get_locale():
    """Chooses the language translation for user."""
    lang = request.args.get('locale', None)
    supported_langs = app.config['LANGUAGES']
    if lang in supported_langs:
        return lang
    return request.accept_languages.best_match(supported_langs)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Root path for app
    """
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
