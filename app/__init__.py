import os

from flask import Flask

from app.extensions import mongo, mail
from app.website import website


def create_app(config_object='app.settings'):
    app = Flask(__name__)
    app.config.from_object(config_object)

    mongo.init_app(app)
    mail.init_app(app)

    app.register_blueprint(website)

    return app
