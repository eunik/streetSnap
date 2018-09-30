import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from database.database import Base, db_session
from database.models import Post

def create_post(user_id, lat, lon, body, artist, img_url="null"):
	p = Post(user_id, lat, lon, body, img_url)
	db_session.add(p)
	# make sure we update our database is updated with the id
	db_session.flush()
	db_session.commit()
	return {'success': 1, 'id': p.id, 'msg': 'success'}

def get_posts():
	json = []
	for post in db_session.query(Post.id, Post.user_id, Post.body, Post.artist, Post.pub_date, Post.img_url):
		json.append({'id' : post.id, 'user_id' : post.user_id, 'body' : post.body, 'artist': post.artist, 'pub_date' : post.pub_date, 'img_url' : post.img_url})
	return {'success': 1, 'locs':json , 'msg': 'success'}
		
def get_locs():
	json = []
	for post in db_session.query(Post.id, Post.artist, Post.lat, Post.lon):
		json.append({'id': post.id, 'artist': post.artist, 'loc':{'lat': post.lat, 'lon': post.lon}})
	return {'success': 1, 'locs':json , 'msg': 'success'}


#print(create_post(1, 1000, 100, "dsf", 'https://lh5.googleusercontent.com/p/AF1QipPwtpYhzEyqEa45JwsYzV8_CC7IHdKcTD1gnHdI=w408-h544-k-no'))
#print(create_post(1, 1000, 100, "dsf"))
#print(get_posts())