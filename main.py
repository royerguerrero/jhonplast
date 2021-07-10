from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/contacto/')
def contact():
    return render_template('contact.html')

@app.route('/productos/<category>/')
def products(category):
    return f'Category: {category}'