from dateutil.parser import parse
from flask import Blueprint, jsonify, abort, request
from flask.ext.jwt import jwt_required, current_user
from flask.views import MethodView
from sqlalchemy import func
from caloric.db import db
from caloric.forms.entry import AddEntryForm
from caloric.models.entry import Entry

entry = Blueprint('entry', __name__, url_prefix='/entry')


class EntryApi(MethodView):

    decorators = [jwt_required()]

    def get_all(self):
        entries = [{'id': entry.id, 'text': entry.text, 'calories': entry.calories, 'datetime': entry.datetime.isoformat()} for entry in current_user.entries]
        return jsonify(entries=entries)

    def get_one(self, entry_id):
        entry = Entry.query.get(entry_id)
        if entry.user_id == current_user.id:
            return jsonify(entry=entry.to_dict())
        abort(403)

    def get(self, entry_id=None):
        if not entry_id:
            return self.get_all()
        else:
            return self.get_one(entry_id)

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
        entry = Entry.query.get(entry_id)
        if entry.user_id == current_user.id:
            entry.delete()
            return jsonify(message='success')
        abort(403)

    def update_entry(self, entry_id):
        entry = Entry.query.get(entry_id)
        if entry.user_id != current_user.id:
            abort(403)
        else:
            data = request.get_json()
            entry.text = data['text']
            entry.calories = data['calories']
            entry.datetime = data['datetime']
            entry.save()
            return jsonify(entry=entry.to_dict())


entry.add_url_rule('/', view_func=EntryApi.as_view('entries'))
entry.add_url_rule('/<int:entry_id>/', view_func=EntryApi.as_view('entry'))


class EntrySearch(MethodView):

    decorators = [jwt_required()]

    def get(self):
        startDate = parse(request.args['startDate']).replace(tzinfo=None)
        endDate = parse(request.args['endDate']).replace(tzinfo=None)
        results = []
        for row in db.session.execute("SELECT DATE(_datetime) AS _datetime, SUM(calories) FROM entry WHERE _datetime BETWEEN :startDate AND :endDate GROUP BY DATE(_datetime)", dict(startDate=startDate, endDate=endDate)):
            dt = parse(row[0]).replace(tzinfo=None).isoformat()
            results.append((dt, row[1]))
        return jsonify(results=results)


entry.add_url_rule('/search/', view_func=EntrySearch.as_view('search'))
