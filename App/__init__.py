from flask import Flask
import os


def create_app():
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY='mykey'
    )

    from . import db

    db.init_app(app)

    from . import reg

    app.register_blueprint(reg.bp)

    return app
