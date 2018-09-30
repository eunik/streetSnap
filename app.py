from flask import Flask, jsonify, request
import streetSnap.database.models as models
import user.user as user
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
	
if __name__ == '__main__':
    app.run()