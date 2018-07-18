import os


DEBUG = True
# IGNORE_AUTH = True
SECRET_KEY = 'the-secret!'
basedir = os.path.abspath(os.path.dirname(__file__))

SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
                          'sqlite:///' + \
                          os.path.join(basedir,
                                       '../data-dev.sqlite3')
#?check_same_thread=False')

SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_RECORD_QUERIES = True
