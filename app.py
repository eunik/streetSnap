import os
from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
import models

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

@app.route('/user/create-user', methods=['POST'])
def create_new_user():
	"""
	This function creates a new user
	"""
	input = request.get_json()
	return (jsonify(create_user.create_user(input["username"], input["password"], input["first"], input["last"])), 200)

@app.route('/user/get/id/<int:id>/key/<string:key>', methods=['GET'])
def grab_user_info(id, key):
	"""
	This function will get information from a user
	"""
	input = request.get_json()
	return (jsonify(get_user_info.get_user_info(id, key)), 200	
	
if __name__ == '__main__':
    app.run()