from flask import Blueprint, jsonify, abort
from flask.ext.jwt import jwt_required, current_user
from flask.views import MethodView

entry = Blueprint('entry', __name__, url_prefix='/entry')


class EntryApi(MethodView):

    decorators = [jwt_required()]

    def get(self, entry_id=None):
        if not entry_id:
            entries = [{'id': entry.id, 'text': entry.text, 'calories': entry.calories, 'datetime': entry.datetime} for entry in current_user.entries]
            return jsonify(entries=entries)
        else:
            for entry in current_user.entries:
                if entry.id == entry_id:
                    return jsonify(entry=entry.to_dict())
            abort(400)

    def post(self, entry_id=None):
        pass

    def delete(self, entry_id):
        pass


entry.add_url_rule('/', view_func=EntryApi.as_view('entries'))
entry.add_url_rule('/<int:entry_id>/', view_func=EntryApi.as_view('entry'))
