from flask.ext.jwt import JWT
from sqlalchemy.orm.exc import NoResultFound
from caloric.models.user import User, bcrypt

__author__ = 'Marcus McCurdy'

jwt = JWT()

@jwt.user_handler
def load_user(payload):
    return User.query.get(payload['id'])

@jwt.payload_handler
def payload_handler(user):
    return dict(id=user.id, email=user.email)


@jwt.authentication_handler
def authenticate(username, password):
    try:
        db_user = User.query.filter_by(email=username).one()
    except NoResultFound:
        pass
    else:
        if bcrypt.check_password_hash(db_user.password, password):
            return db_user
    return None


