#!/usr/bin/env python3
"""
Defines a flask app.
"""
from flask_babel import Babel
from flask import Flask, render_template

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

@app.route('/', strict_slashes=False)
def index() -> str:
    """
    Root path for app
    """
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(port=5000, host="0.0.0.0", debug=True)
