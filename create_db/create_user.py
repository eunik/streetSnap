from app import db
from sqlalchemy.dialects.postgresql import JSON


class New_user(db.Model):
    __tablename__ = 'new_user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String())
    first = db.Column(db.String())
	last = db.Column(db.String())

    def __init__(self, username, first, last):
        self.username = username
        self.first = first
        self.last = last
	
	

    def __repr__(self):
        return '<id {}>'.format(self.id)