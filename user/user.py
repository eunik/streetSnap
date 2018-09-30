import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from database.database import Base
from database.database import db_session
from database.models import User

def create_user(username, password, first, last):
	if len(password) > 16:
		return {'success': 0, 'id': 'null', 'msg': 'password is too long, make less than 16'}
	u = User(username, password, first, last)
	if db_session.query(User).filter(User.username == username).first():
		return {'success': 0, 'id': 'null', 'msg': 'user already exist'}
	db_session.add(u)
	db_session.flush()
	db_session.commit()
	return {'success': 1, 'id': u.id, 'msg': 'success'}

def get_user_info(id, key):
	u = db_session.query(User).get(id)
	value = getattr(u, key)
	return {'id': 'id', str(key): value}
	
def remove_user(id):
	User.query.filter_by(id=id).delete()
	
#print(create_user('dax3ddsdddd', 'a', 'a', 'a'))
#print(get_user_info('1','username'))
#remove_user(7)