import csv
from app.models import Product

def run():
    """
    Reads the products.csv and returns a list of serialized products
    to be appened into db
    
    Note: To run this script you must import it from flask shell
    """
    with open('products.csv', mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        products = []
        for row in csv_reader:
            if line_count == 0:
                line_count += 1
            
            if row['capacity'] == '':
                products.append(Product(name=row['name'], price=row['price'], image=row['image'], heigth=row['dimentions.heigth'], width=row['dimentions.width'], length=row['dimentions.length'], category=row['category']))
            else:
                products.append(Product(name=row['name'], price=row['price'], image=row['image'], capacity=row['capacity'], category=row['category']))

            line_count += 1

        return products
