#! /usr/bin/python

import os
from app import create_app

if __name__ == '__main__' or __name__ == 'run':
    app = create_app(os.environ.get('FLASK_CONFIG', 'development'))
    with app.app_context():
        pass

    app.run()