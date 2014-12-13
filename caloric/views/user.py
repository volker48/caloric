from flask import Blueprint, request, jsonify, abort
from flask.ext.login import login_user
from flask.views import MethodView
from sqlalchemy.orm.exc import NoResultFound
from caloric.models.user import User, bcrypt
from caloric.forms.user import SignupForm, UserSettingsForm

user = Blueprint('user', __name__, url_prefix='/user')


class UserApi(MethodView):

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
    

class SignIn(MethodView):

    def post(self):
        #TODO: Don't like this duplication. This looks too similar to the post method in SignupApi
        form = SignupForm(data=request.get_json(silent=True))
        if form.validate():
            try:
                db_user = User.query.filter_by(email=form.email.data).one()
            except NoResultFound:
                return jsonify(error='Invalid email/password')
            if bcrypt.check_password_hash(db_user.password, form.password.data):
                login_user(db_user)
                return jsonify(success='Logged in')
            else:
                return jsonify(error='Invalid email/password')
        else:
            return jsonify(**form.errors)


user.add_url_rule('/login/', view_func=SignIn.as_view('login'))


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

