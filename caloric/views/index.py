from flask import Blueprint, render_template
from flask.views import MethodView

__author__ = 'Marcus McCurdy'


index = Blueprint('index', __name__)


class IndexView(MethodView):

    def get(self):
        return render_template('index.html')

index.add_url_rule('/', view_func=IndexView.as_view('index'))


