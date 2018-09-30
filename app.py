from flask import Flask, jsonify, request
import database.models as models
import user.user as user
import user.follower as follower
import post.post as post
import datetime
time_compiled = datetime.datetime.now()

app = Flask(__name__)

# test_run: https://
@app.route('/')
def flask_creation():
	"""
	Getting date of when it was last modified
	args: none
	returns: message of compilation (string)
	"""
	return ("API UP AND RUNNING, LAST COMPILED AT: {}".format(str(time_compiled)), 200)

@app.route('/user/create-user', methods=['POST'])
def create_new_user():
	"""
	This function creates a new user
	"""
	input = request.get_json()
	return (jsonify(user.create_user(input["username"], input["password"], input["first"], input["last"])), 200)

# http://127.0.0.1:5000/user/get/id/1/key/username
@app.route('/user/get/id/<int:id>/key/<string:key>', methods=['GET'])
def grab_user_info(id, key):
	"""
	This function will get information from a user
	"""
	return (jsonify(user.get_user_info(id, key)), 200)
	
@app.route('/post/create-post', methods=['POST'])
def create_new_post():
	"""
	This function creates a new post
	"""
	input = request.get_json()
	return (jsonify(post.create_post(input["user_id"], input["lat"], input["lon"], input["body"])), 200)

# http://127.0.0.1:5000/post/get/locs/
@app.route('/post/get/locs/', methods=['GET'])
def grab_locs():
	"""
	This function will get information from a post
	"""
	return (jsonify(post.get_locs()), 200)
	

# http://127.0.0.1:5000/post/get/post/
@app.route('/post/get/post/', methods=['GET'])
def grab_post():
	"""
	This function will get information from a post
	"""
	return (jsonify(post.get_posts()), 200)
	
@app.route('/post/create-follow', methods=['POST'])
def create_new_follow():
	"""
	This function creates a new post
	"""
	input = request.get_json()
	return (jsonify(post.create_post(input["from_id"], input["to_id"])), 200)
	
	
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)