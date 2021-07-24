import os

MONGO_URI = os.environ.get('MONGO_URI')
MAIL_SERVER = os.environ.get('MAIL_SERVER')
MAIL_PORT = os.environ.get('MAIL_PORT')
MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
MAIL_USE_SSL = os.environ.get('MAIL_USE_SSL')
MAIL_DEFAULT_SENDER = os.environ.get('MAIL_DEFAULT_SENDER')
SECRET_KEY = os.environ.get('SECRET_KEY')