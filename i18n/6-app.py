#!/usr/bin/env python3
"""
Basic Flask app using Babel
"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from typing import Dict


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
    return render_template("6-index.html", username=g.user)


def get_locale() -> str:
    """ get local languages """
    locale = request.args.get("locale")
    if (locale is not None and locale in Config.LANGUAGES):
        return locale

    if g.user:
        user_locale = g.user.get("locale")
        if user_locale and user_locale in Config.LANGUAGES:
            return user_locale

    header = request.headers.get('locale')
    if header:
        return header

    return request.accept_languages.best_match(Config.LANGUAGES)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Dict:
    """Get the user based to query parameter
    """
    login_as = request.args.get("login_as")
    if login_as is None:
        return None

    try:
        id = int(login_as)
    except ValueError:
        return None

    return users.get(id)


@app.before_request
def before_request():
    """Setup app state before every request
    """
    user = get_user()
    g.user = None
    if user is not None:
        g.user = user


babel = Babel(app, locale_selector=get_locale)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001)
