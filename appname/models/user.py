from .db import db, ActiveModel
from .core import Base
from flask.ext.login import UserMixin, AnonymousUserMixin
from flask.ext.bcrypt import check_password_hash, generate_password_hash

class User(Base, ActiveModel, UserMixin):
    username = db.Column(db.String, unique=True)
    password = db.Column(db.String)

    def __init__(self, username, password):
        self.username = username
        self.password = generate_password_hash(password)

    def is_authenticated(self):
        if isinstance(self, AnonymousUserMixin):
            return False
        else:
            return True

    def is_active(self):
        return True

    def is_anonymous(self):
        if isinstance(self, AnonymousUserMixin):
            return True
        else:
            return False

    def get_id(self):
        return self.id

    @classmethod
    def authenticate(cls, username, password):
        user = User.query.filter_by(username=username).first()
        return user if check_password_hash(user.password, password) else None
    
    def __repr__(self):
        return '<User %r>' % self.username
