from datetime import datetime
from .db import db

# Define Base model that other models can extend
class Base(db.Model):
    __abstract__ = True

    # All tables will have primary key ID, date created, and date modified columns
    id = db.Column(db.Integer, primary_key=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(), onupdate=db.func.current_timestamp())