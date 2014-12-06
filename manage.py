#!/usr/bin/env python

from flask.ext.script import Manager
from caloric.app import create_app

app = create_app()
app.debug = True

manager = Manager(app)

if __name__ == '__main__':
    manager.run()