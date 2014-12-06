from flask import Blueprint
from flask.views import MethodView

__author__ = 'Marcus McCurdy'


index = Blueprint('index', __name__)

class IndexView(MethodView):

    def get(self):
        return 'hello'

index.add_url_rule('/', view_func=IndexView.as_view('index'))


