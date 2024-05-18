#!/usr/bin/env python3
"""
Defines a flask app.
"""
from flask_babel import Babel
from flask import (
    Flask,
    render_template,
    request
    )


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


@babel.localeselector
def get_locale():
    """Chooses the language translation for user."""
    lang = request.args.get('locale', None)
    supported_langs = app.config['LANGUAGES']
    print(lang)
    if lang in supported_langs:
        return lang
    return request.accept_languages.best_match(supported_langs)


@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Root path for app
    """
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
