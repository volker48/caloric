#!/usr/bin/env python

from flask.ext.script import Manager, Shell
from caloric.app import create_app
from caloric.db import db
from caloric.models.entry import Entry
from caloric.models.user import User

app = create_app()
app.debug = True

manager = Manager(app)

@manager.command
def create_tables():
    db.create_all(app=app)


def _make_context():
    return {
        'Entry': Entry,
        'User': User
    }

manager.add_command('shell', Shell(make_context=_make_context, use_ipython=True))

if __name__ == '__main__':
    manager.run()