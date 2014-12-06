__author__ = 'Marcus McCurdy'

from views.index import index


def register(app):
    app.register_blueprint(index)
