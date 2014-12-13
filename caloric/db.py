from sqlalchemy.exc import SQLAlchemyError

__author__ = 'Marcus McCurdy'


from flask.ext.sqlalchemy import SQLAlchemy


db = SQLAlchemy()


class ActiveModel(object):

    def save(self, commit=True):

        db.session.add(self)

        if commit:
            try:
                db.session.commit()
            except SQLAlchemyError as exc:
                db.session.rollback()
                raise exc

        return self

