#!/usr/bin/env python3
"""
Basic Flask app using Babel
"""
from flask import Flask, render_template, request
from flask_babel import Babel


class Config():
    """ Config class for babel """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)


@app.route("/")
def index():
    """ index """
    return render_template("4-index.html")


def get_locale() -> str:
    """ get local languages """
    locale = request.args.get("locale")
    if locale in Config.LANGUAGES:
        return locale

    return request.accept_languages.best_match(Config.LANGUAGES)


babel = Babel(app, locale_selector=get_locale)

if __name__ == "__main__":
    app.run()
