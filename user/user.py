import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from database.database import Base, db_session
from database.models import User

def create_user(username, password, first, last, img_url="null"):
	if len(password) > 16:
		return {'success': 0, 'id': 'null', 'msg': 'password is too long, make less than 16'}
	u = User(username, password, first, last, img_url)
	
	# make sure it is not duplicate
	if db_session.query(User).filter(User.username == username).first():
		return {'success': 0, 'id': 'null', 'msg': 'user already exist'}
	db_session.add(u)
	# make sure we update our database is updated with the id
	db_session.flush()
	db_session.commit()
	return {'success': 1, 'id': u.id, 'msg': 'success'}

def get_user_info(id, key):
	u = db_session.query(User).get(id)
	value = getattr(u, key)
	return {'id': str(id), key: str(value)}
	
def get_user(id):
	u = db_session.query(User).get(id)
	return {'id': str(u.id), 'username': str(u.username), 'name': '{} {}'.format(u.first, u.last), 'img_url': str(u.img_url)}
	
def remove_user(id):
	User.query.filter_by(id=id).delete()
	
#print(create_user('a', 'a', 'Jack', 'Sparow', 'http://i376.photobucket.com/albums/oo208/vldesai/Picture001.jpg'))
#print(create_user('b', 'b', 'Macho', 'Man', 'http://i793.photobucket.com/albums/yy212/mrsexxy2010/Picture0136.jpg'))
#print(get_user(1))
#print(get_user_info('1','username'))
#remove_user(7)