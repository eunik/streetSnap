from sqlalchemy import Column, Integer, String
from database import Base
from database import db_session

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	username = Column(String(50), unique=True)
	first = Column(String(50))
	last = Column(String(50))
	password= Column(String(128))
	salt= Column(String(32))

	def __init__(self, username, password, first, last):
		self.username = username
		self.password = password
		self.first = first
		self.last = last

	def __repr__(self):
		return '<User %r>' % (self.user)