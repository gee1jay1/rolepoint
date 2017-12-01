from flask import Flask

from contact_search import contact_search_bp

def create_app():
    app = Flask(__name__)

    app.secret_key = 'some_secret'

    app.register_blueprint(contact_search_bp)

    return app
