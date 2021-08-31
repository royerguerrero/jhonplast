from flask import Flask

from app.extensions import db, mail
from app.website import website


def create_app(config_object='app.settings'):
    app = Flask(__name__)
    app.config.from_object(config_object)

    app.app_context().push()

    db.init_app(app)
    db.create_all()

    mail.init_app(app)

    app.register_blueprint(website)

    return app
