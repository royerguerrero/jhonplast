import os

from flask import Flask, render_template, request

from app.extensions import mongo, mail
from app.api import api


def create_app(config_object='app.settings'):
    app = Flask(__name__)
    app.config.from_object(config_object)

    mongo.init_app(app)
    mail.init_app(app)

    app.register_blueprint(api)

    @app.route('/')
    def index():
        return render_template('index.html')

    @app.route('/contacto/')
    def contact():
        return render_template('contact.html')

    @app.route('/productos/')
    def products():
        return render_template('products.html')

    return app
