from flask import Blueprint, jsonify, abort, request
from flask.ext.jwt import jwt_required, current_user
from flask.views import MethodView
from caloric.forms.entry import AddEntryForm
from caloric.models.entry import Entry

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

    def create_entry(self):
        form = AddEntryForm(data=request.get_json(silent=True))
        if not form.validate():
            return jsonify(**form.errors)
        else:
            new_entry = Entry(form.text.data, form.calories.data, form.datetime.data)
            new_entry.user_id = current_user.id
            new_entry.save()
            return jsonify(entry=new_entry.to_dict())

    def post(self, entry_id=None):
        if entry_id:
            return self.update_entry(entry_id)
        else:
            return self.create_entry()

    def delete(self, entry_id):
        pass

    def update_entry(self, entry_id):
        pass


entry.add_url_rule('/', view_func=EntryApi.as_view('entries'))
entry.add_url_rule('/<int:entry_id>/', view_func=EntryApi.as_view('entry'))
