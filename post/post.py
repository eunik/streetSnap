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

def create_post(user_id, lat, lon, body):
	p = Post(user_id, lat, lon, body)

	db_session.add(p)
	# make sure we update our database is updated with the id
	db_session.flush()
	db_session.commit()
	return {'success': 1, 'id': p.id, 'msg': 'success'}

def displayPosts():
    for post in db_session.query(Post.id):
        print(Post.id)

print(create_post(788, 107.87, 376.9789785, ' the body'))
displayPosts()
