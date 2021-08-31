from flask import Blueprint, render_template, request, flash
from flask_mail import Message
from app.extensions import mail
from app.models import Product

website = Blueprint('website', __name__)


@website.route('/')
def index():
    return render_template('index.html')


@website.route('/contacto/', methods=['GET', 'POST'])
def contact():
    error = None
    if request.method == 'POST':
        if request.form['name'] == '':
            error = 'Asegurese de ingresar su nombre'
        elif request.form['phone_number'] == '':
            error = 'Asegurese de añadir su numero de telefono'
            # TODO: add regex validation for the number phone
        elif request.form['message'] == '':
            error = 'Asegurese de incluir el mensaje'
        else:
            msg = Message('Hello', recipients=['ventas@jhonplast.com'])
            mail.send(msg)
            phone_number = request.form['phone_number']
            flash(f'Su mensaje fue enviado satisfactoriamente, pronto resivira respuesta a su numero {phone_number}')

    return render_template('contact.html', error=error)


@website.route('/productos/')
def products():
    products = []

    category = request.args.get('category', None)
    search = request.args.get('s', None)
    if category is not None:
        products = Product.query.filter_by(category=category)

    if search is not None:
        products = Product.query.filter(Product.name.ilike(f'%{search}%'))

    return render_template('products.html', products=products)
