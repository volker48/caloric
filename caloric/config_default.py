from datetime import timedelta

SECRET_KEY = 'abc123notreallysecret'
SQLALCHEMY_DATABASE_URI = 'sqlite:///caloric.db'
WTF_CSRF_ENABLED = False
JWT_EXPIRATION_DELTA = timedelta(days=1)