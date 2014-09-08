from datetime import datetime
from .db import db

# Define a base model for singular models that can be extended
class SingularModel(db.Model):
    __abstract__ = True

    # All tables will have primary key ID, date created, and date modified columns
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())