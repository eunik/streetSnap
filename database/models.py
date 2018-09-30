import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from sqlalchemy import Column, Integer, String, Float, Date, Text, DateTime
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
	
	__table_args__ = {'extend_existing': True} 

	def __init__(self, username, password, first, last):
		self.username = username
		self.password = password
		self.first = first
		self.last = last
	
	def get_item(self, parameter):
		if parameter == 'all':
			return {'id': self.id, 'username': self.username,
				'first': self.first, 'last': self.last, 'self.password': self.password}
		
		return {parameter: str(getattr(self, parameter))}

	def __repr__(self):
		return '<User %r>' % (self.id)
		
		
class Post(Base):
	__tablename__ = 'posts'
	id = Column(Integer, primary_key=True)
	user_id = Column(Integer)
	body = Column(Text, nullable=False)
	pub_date = Column(DateTime, nullable=False, default=datetime.datetime.utcnow)
	lat = Column(Float(Precision=64))
	lon = Column(Float(Precision=64))
	
	# extends existing table if it exists
	__table_args__ = {'extend_existing': True} 

	def __init__(self, user_id, lat, lon, body = ""):
		self.user_id = user_id
		self.body = body
		self.lat = lat
		self.lon = lon
		
	def __repr__(self):
		return '<Post %r>' % (self.id)
		
class Follow(Base):
	__tablename__ = 'follows'
	from_id = Column(Integer, primary_key=True)
	to_id = Column(Integer, primary_key=True)

	# extends existing table if it exists
	__table_args__ = {'extend_existing': True} 
	
	def __init__(self, from_id, to_id):
		self.from_id = from_id
		self.to_id = to_id

	def __repr__(self):
		return '<Follow %r%r>' % (self.from_id, self.to_id)

		
		