from flask import Blueprint, request, jsonify, abort
from flask.ext.jwt import jwt_required
from flask.views import MethodView
from caloric.models.user import User
from caloric.forms.user import SignupForm, UserSettingsForm

user = Blueprint('user', __name__, url_prefix='/user')


class UserApi(MethodView):

    decorators = [jwt_required()]

    def _base(self, user_id):
        u = User.query.get(user_id)
        if not u:
            abort()
        return u

    def get(self, user_id):
        usr = self._base(user_id)
        return jsonify(email=usr.email, daily_calories=usr.daily_calories)

    def post(self, user_id):
        usr = self._base(user_id)
        form = UserSettingsForm(data=request.get_json(silent=True))
        if form.validate():
            usr.daily_calories = form.daily_calories.data
            usr.save()
        else:
            return jsonify(**form.errors)


user.add_url_rule('/<int:user_id>/', view_func=UserApi.as_view('user'))


class SignupApi(MethodView):

    def post(self):
        form = SignupForm(data=request.get_json(silent=True))
        if form.validate():
            existing_user = User.query.filter_by(email=form.email.data).first()
            if existing_user:
                data = {'error': 'Email already registered'}
            else:
                new_user = User(form.email.data, form.password.data)
                new_user.save()
                data = {'success': new_user.id}
        else:
            data = form.errors
        return jsonify(**data)



user.add_url_rule('/signup/', view_func=SignupApi.as_view('signup'))

