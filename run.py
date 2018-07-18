#! /usr/bin/python

import os
from app import create_app, db
from app.models import User, Item

if __name__ == '__main__' or __name__ == 'run':
    app = create_app(os.environ.get('FLASK_CONFIG', 'development'))
    with app.app_context():
        pass

    app.run()

    @app.shell_context_processor
    def make_shell_context():
        return {'db': db, 'User': User, 'Item': Item}