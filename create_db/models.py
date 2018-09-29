from sqlalchemy import Column, Integer, String, Float, Date
from database import Base
from database import db_session
import datetime

class User(Base):
	__tablename__ = 'users'
	id = Column(Integer, primary_key=True)
	username = Column(String(50), unique=True)
	first = Column(String(50))
	last = Column(String(50))
	password= Column(String(12))

	def __init__(self, username, password, first, last):
		self.username = username
		self.password = password
		self.first = first
		self.last = last

	def __repr__(self):
		return '<User %r>' % (self.user)
		
		
class Post(Base):
	__tablename__ = 'posts'
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer)
	description = Column(String(256))
	lat = Column(Float(Precision=64))
	lon = Column(Float(Precision=64))
	date = Column(Date)

	def __init__(self, user_id, description, lat, lon):
		self.user_id = user_id
		self.description = description
		self.lat = lat
		self.lon = lon
		self.date = datetime.date.today()

	def __repr__(self):
		return '<Post %r>' % (self.post)
		
		