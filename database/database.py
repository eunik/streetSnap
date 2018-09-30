import os
from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

#engine = create_engine('postgresql+psycopg2://postgres:postgre@localhost:5432/streetSnap')
engine = create_engine('postgresql+psycopg2://postgres:streetart@35.224.228.122:5432/', echo=True)
db_session = scoped_session(sessionmaker(autocommit=False,
										 autoflush=False,
										 bind=engine))
Base = declarative_base()
Base.query = db_session.query_property()

def init_db():
	# import all modules here that might define models so that
	# they will be registered properly on the metadata.  Otherwise
	# you will have to import them first before calling init_db()
	import models
	
	Base.metadata.create_all(bind=engine)