from flask import Flask, render_template, request
from app.api import api


app = Flask(__name__)
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
