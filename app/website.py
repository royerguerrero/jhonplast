from flask import Blueprint, render_template, request
from flask_mail import Message
from app.extensions import mail

website = Blueprint('website', __name__)


@website.route('/')
def index():
    return render_template('index.html')


@website.route('/contacto/', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        msg = Message('Hello', recipients=['ventas@jhonplast.com'])
        mail.send(msg)

    return render_template('contact.html')


@website.route('/productos/')
def products():
    return render_template('products.html')
