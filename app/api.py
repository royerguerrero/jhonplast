from flask import Blueprint, Response
from app.extensions import mongo
from bson import json_util

api = Blueprint('api', __name__, url_prefix='/api/')


@api.route('/products/', methods=['GET'])
def products():
    return 'Products endpoint...'
