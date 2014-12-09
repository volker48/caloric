__author__ = 'Marcus McCurdy'

from views.index import index
from views.user import user

def register(app):
    app.register_blueprint(index)
    app.register_blueprint(user)
