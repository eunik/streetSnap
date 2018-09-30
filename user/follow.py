import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from database.database import Base, db_session
from database.models import Follow

def follow(from_id, to_id):
	# assume my_id and friend_id are valid
	u = Follow(from_id, to_id)
	db_session.add(u)
	db_session.flush()
	db_session.commit()
	return {'success': 1, 'from_id': u.from_id, 'to_id': u.u_id, 'msg': 'success'}
	
#print(create_post(1, 1000, 100, "dsf"))