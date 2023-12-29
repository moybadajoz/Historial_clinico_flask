from flask import Flask
import os


def create_app():
    app = Flask(__name__)

    from . import db

    db.init_app(app)

    from . import registros

    app.register_blueprint(registros.bp)

    return app
