from app.extensions import db

CATEGORY_CHOICES = ('estibas', 'canastillas', 'canecas', 'postes')

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    price = db.Column(db.String(30))
    image = db.Column(db.String(255))

    capacity = db.Column(db.String(5), nullable=True)
    heigth = db.Column(db.String(5), nullable=True)
    width = db.Column(db.String(5), nullable=True)
    length = db.Column(db.String(5), nullable=True)

    category = db.Column(db.Enum(*CATEGORY_CHOICES))