import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from database.database import Base
from database.database import db_session
from database.models import Post

def get_locs():
	locs = [[post.lat, post.lon] for post in Post.query.all()]
	print (locs)
	#return {'success': 1, 'id': u.id, 'msg': 'success'}

get_locs()
	
#print(create_user('dax3ddsdddd', 'a', 'a', 'a'))
#print(get_user_info('1','username'))
#remove_user(7)