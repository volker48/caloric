from flask import Blueprint, request, jsonify
from flask.views import MethodView
from caloric.models.user import User
from caloric.forms.user import SignupForm

user = Blueprint('user', __name__, url_prefix='/user')


class UserApi(MethodView):

    def get(self, user_id):
        pass

    def post(self, user_id):
        pass


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


user.add_url_rule('/<int:user_id>/', view_func=UserApi.as_view('user'))
user.add_url_rule('/signup/', view_func=SignupApi.as_view('signup'))

